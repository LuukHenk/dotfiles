
from typing import List, Final, Optional

from package_installer.data_models.version_enum import Version
from package_installer.data_models.package_info import PackageInfo
from package_installer.data_models.manager_enum import ManagerEnum
from package_installer.package_managers_handlers.package_manager_handler import PackageManagerHandler

class AptPackageManagerHandler(PackageManagerHandler):
    INFO_COMMAND: Final[List[str]] = ["apt", "info"]
    INSTALLED_COMMAND: Final[List[str]] = ["dpkg-query", "-l"]
    VERSION_INDICATOR: Final[str] = "\nVersion: "
    
    def find_package(self, package_name: str) -> List[PackageInfo]:
        
        latest_version_str = self.__find_latest_package_version(package_name)
        installed_version_str = self.__find_installed_version(package_name)
        
        packages: List[PackageInfo] = []
        latest_package_installed = self.__check_if_latest_package_is_installed(
            latest_version=latest_version_str,
            installed_version=installed_version_str    
        )
        
        if latest_version_str is not None:
            packages.append(PackageInfo(
                name=package_name,
                version=(latest_version_str, Version.LATEST_STABLE),
                installed=latest_package_installed,
                manager=ManagerEnum.APT,
            ))
            
        if installed_version_str is not None and not latest_package_installed:
            packages.append(PackageInfo(
                name=package_name,
                version=(installed_version_str, Version.OTHER),
                installed=True,
                manager=ManagerEnum.APT,
            ))

        return packages
        
    def __find_latest_package_version(self, package_name: str) -> Optional[str]:
        command = self.INFO_COMMAND + [package_name]
        latest_version = self.__find_version(command, self.VERSION_INDICATOR)
        if not latest_version:
            return None
        return latest_version.split("\n")[0]
    
    def __find_installed_version(self, package_name: str) -> Optional[str]:
        command = self.INSTALLED_COMMAND + [package_name]
        installed_version = self.__find_version(command, package_name)
        if not installed_version:
            return None
        return installed_version.strip().split()[0]

    def __find_version(self, command: List[str], version_indicator: str) -> Optional[str]:
        package_info = self._run_command(command)
        if package_info.returncode != 0 or not version_indicator in package_info.stdout:
            return None
        return package_info.stdout.split(version_indicator)[1]
    
    @staticmethod
    def __check_if_latest_package_is_installed(latest_version: Optional[str], installed_version: Optional[str]) -> bool:
        package_installed = False
        if latest_version is not None and installed_version is not None:
            package_installed = latest_version == installed_version
        return package_installed
