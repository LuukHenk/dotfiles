from tomllib import load, TOMLDecodeError
from pathlib import Path
from typing import List, Any, Dict

from configuration_loader.parsers.package_parser_keys import PackageParserKeys as Keys
from data_models.package import Package
from logger.logger import log_error
from package_manager_manager.package_manager_manager import PackageManagerManager


class PackageParser:
    def __init__(self):
        self.__package_manager_manager = PackageManagerManager()

    def parse(self, file_path: Path) -> List[Package]:
        try:
            raw_package_data = self.__load_from_toml(file_path)
            packages = self.__parse_package_data(raw_package_data)
        except (KeyError, TOMLDecodeError) as err:
            log_error(f"Failed to parse packages: {err}")
            return []
        return packages

    @staticmethod
    def __load_from_toml(file_path: Path) -> Dict[str, Any]:
        with open(file_path, "rb") as f:
            data = load(f)
        return data

    def __parse_package_data(self, raw_package_data: Dict[str, Any]) -> List[Package]:
        packages = []
        covered_packages = []
        package_name_to_groups_mapping = self.__map_package_name_and_groups(raw_package_data)
        raw_packages = [package for group in raw_package_data[Keys.PACKAGE_GROUPS] for package in group[Keys.PACKAGES]]
        for package in raw_packages:
            for search_name in package[Keys.SEARCH_NAMES]:
                package_name = package[Keys.NAME]
                if package_name in covered_packages:
                    continue
                covered_packages.append(package_name)
                groups = package_name_to_groups_mapping[package_name]
                search_results = self.__package_manager_manager.find_package(search_name[Keys.NAME])
                for search_result in search_results:
                    packages.append(
                        Package(
                            name=package[Keys.NAME],
                            search_name=search_name[Keys.NAME],
                            groups=groups,
                            manager_name=search_result.manager_name,
                            installed=search_result.package_installed,
                            version=search_result.package_version,
                        )
                    )
        print(packages)
        return packages

    @staticmethod
    def __map_package_name_and_groups(raw_package_data: Dict[str, Any]) -> Dict[str, List[str]]:
        package_name_to_group_name_mapper = {}
        package_groups = raw_package_data[Keys.PACKAGE_GROUPS]
        for group in package_groups:
            group_name = group[Keys.NAME]
            for package in group[Keys.PACKAGES]:
                package_name = package[Keys.NAME]
                if package_name in package_name_to_group_name_mapper:
                    groups = package_name_to_group_name_mapper[package_name]
                    if group_name not in groups:
                        groups.append(group_name)
                    continue
                package_name_to_group_name_mapper[package_name] = [group_name]
        return package_name_to_group_name_mapper
