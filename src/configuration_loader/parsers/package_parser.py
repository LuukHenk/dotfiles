from tomllib import load, TOMLDecodeError
from pathlib import Path
from typing import List, Any, Dict

from configuration_loader.parsers.parser import Parser
from configuration_loader.parsers.package_parser_keys import PackageParserKeys as Keys
from data_models.manager_name import ManagerName
from data_models.package import Package
from logger.logger import log_error
from package_manager_manager.package_manager_manager import PackageManagerManager


class PackageParser(Parser):
    def __init__(self):
        self.__package_manager_manager = PackageManagerManager()

    def parse(self, file_path: Path) -> List[Package]:
        try:
            raw_package_data = self.__load_from_toml(file_path)
            packages = self.__parse_package_data(raw_package_data)
        except (KeyError, TOMLDecodeError) as err:
            log_error(f"Failed to parse packages: {err}")
            return []
        packages = self.__set_correct_group_names(packages)
        return packages

    @staticmethod
    def __load_from_toml(file_path: Path) -> Dict[str, Any]:
        with open(file_path, "rb") as f:
            data = load(f)
        return data

    def __parse_package_data(self, raw_package_data: Dict[str, Any]) -> List[Package]:
        packages = []
        package_groups = raw_package_data[Keys.PACKAGE_GROUPS]
        for group in package_groups:
            for package in group[Keys.PACKAGES]:
                for search_name in package[Keys.SEARCH_NAMES]:
                    search_results = self.__package_manager_manager.find_package(search_name[Keys.NAME])
                    for search_result in search_results:
                        packages.append(
                            Package(
                                name=package[Keys.NAME],
                                search_name=search_name[Keys.NAME],
                                groups=[group[Keys.NAME]],
                                manager_name=search_result.manager_name,
                                installed=search_result.package_installed,
                                version=search_result.package_version,
                            )
                        )
        return packages

    @staticmethod
    def __set_correct_group_names(packages: List[Package]) -> List[Package]:
        package_name_to_group_name_mapper = {}
        for package in packages:
            if package.name in package_name_to_group_name_mapper:
                package_group = package.groups[0]
                groups = package_name_to_group_name_mapper[package.name]
                if package_group not in groups:
                    groups.append(package_group)
                continue
            package_name_to_group_name_mapper[package.name] = package.groups

        for package in packages:
            package.groups = package_name_to_group_name_mapper[package.name]
        return packages
