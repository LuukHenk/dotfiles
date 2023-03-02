
from typing import List, Final, Optional, Tuple

from package_installer.subprocess_interface import run_
from package_installer.data_models.version_enum import Version
from package_installer.data_models.package_info import PackageInfo
from package_installer.data_models.manager_enum import ManagerEnum
from package_installer.package_managers_handlers.package_manager_handler import PackageManagerHandler

class SnapPackageManagerHandler(PackageManagerHandler):
    def find_package(self, package_name: str) -> List[PackageInfo]:
        latest_versions: List[Tuple[str, Version]]  = self.__find_latest_package_versions(package_name)
        installed_version: str = self.__find_installed_version(package_name)
        return self.__generate_package_info(package_name, latest_versions)

    def __find_latest_package_versions(self, package_name: str) -> List[Tuple[str, Version]]:
        pass

    def __find_installed_version(self, package_name: str) -> str:
        pass

    def __generate_package_info(self, package_name: str, latest_versions: List[Tuple[str, Version]]) -> List[PackageInfo]:
        pass