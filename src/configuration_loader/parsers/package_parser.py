from tomllib import load, TOMLDecodeError
from pathlib import Path
from typing import List, Any, Dict, Union

from configuration_loader.parsers.package_parser_keys import PackageParserKeys as Keys
from data_models.package import Package
from logger.logger import log_error
from package_manager_manager.package_manager_manager import PackageManagerManager


class PackageParser:
    CONFIG_PACKAGE_FORMAT = Dict[str, Union[List[str], str]]
    CONFIG_FORMAT = Dict[str, List[CONFIG_PACKAGE_FORMAT]]

    def __init__(self):
        self.__package_manager_manager = PackageManagerManager()
        self.__packages = {}

    def parse(self, file_path: Path) -> List[Package]:
        try:
            raw_packages = self.__load_packages_from_toml(file_path)
            packages = self.__parse_raw_packages(raw_packages)
        except (KeyError, TOMLDecodeError) as err:
            log_error(f"Failed to parse packages: {err}")
            return []
        return packages

    @staticmethod
    def __load_packages_from_toml(file_path: Path) -> List[CONFIG_PACKAGE_FORMAT]:
        with open(file_path, "rb") as f:
            data: PackageParser.CONFIG_FORMAT = load(f)
        return [package for package in data[Keys.PACKAGES]]

    def __parse_raw_packages(self, raw_packages: List[CONFIG_PACKAGE_FORMAT]) -> List[Package]:
        packages = []
        for raw_package in raw_packages:
            packages += self.__parse_raw_package(raw_package)
        return packages

    def __parse_raw_package(self, raw_package: CONFIG_PACKAGE_FORMAT) -> List[Package]:
        packages = []
        for search_name in raw_package[Keys.SEARCH_NAMES]:
            search_results = self.__package_manager_manager.find_package(search_name)
            for search_result in search_results:
                package = Package(
                    name=raw_package[Keys.NAME],
                    search_name=search_name,
                    groups=raw_package[Keys.GROUPS],
                    manager_name=search_result.manager_name,
                    installed=search_result.package_installed,
                    version=search_result.package_version,
                )
                packages.append(package)
        return packages
