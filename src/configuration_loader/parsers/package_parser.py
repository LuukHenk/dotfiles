from typing import List

from configuration_loader.data_models.config_format import ConfigFormat, ItemFormat
from configuration_loader.data_models.config_keys import ConfigKeys
from data_models.package import Package
from package_manager_manager.package_manager_manager import PackageManagerManager


class PackageParser:
    def __init__(self):
        self.__package_manager_manager = PackageManagerManager()

    def parse_packages_config(self, config: ConfigFormat) -> List[Package]:
        packages = []
        for raw_package in config[ConfigKeys.PACKAGES]:
            packages += self.__parse_package(raw_package)
        return packages

    def __parse_package(self, config_package: ItemFormat) -> List[Package]:
        packages = []
        for search_name in config_package[ConfigKeys.SEARCH_NAMES]:
            search_results = self.__package_manager_manager.find_package(search_name)
            for search_result in search_results:
                package = Package(
                    name=config_package[ConfigKeys.NAME],
                    search_name=search_name,
                    group=config_package[ConfigKeys.GROUP],
                    manager_name=search_result.manager_name,
                    installed=search_result.package_installed,
                    version=search_result.package_version,
                    installation_request=False,
                )
                packages.append(package)
        return packages
