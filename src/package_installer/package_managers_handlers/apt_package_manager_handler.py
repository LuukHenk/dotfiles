
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
                version=(latest_version_str, Version.OTHER),
                installed=latest_package_installed,
                manager=ManagerEnum.APT,
            ))

        return packages
        
    def __find_latest_package_version(self, package_name: str) -> Optional[str]:
        package_info = self._run_command(self.INFO_COMMAND + [package_name])
        if package_info.returncode != 0 or not self.VERSION_INDICATOR in package_info.stdout:
            return None
        
        return package_info.stdout.split(self.VERSION_INDICATOR)[1].split("\n")[0]
    
    def __find_installed_version(self, package_name: str) -> Optional[PackageInfo]:
        installation_info = self._run_command(self.INSTALLED_COMMAND + [package_name])
        if not installation_info.returncode == 0 or not package_name in installation_info.stdout:
            return None
        return installation_info.stdout.split(package_name)[1].strip().split()[0]

    @staticmethod
    def __check_if_latest_package_is_installed(latest_version: Optional[str], installed_version: Optional[str]) -> bool:
        package_installed = False
        if latest_version is not None and installed_version is not None:
            package_installed = latest_version == installed_version
        return package_installed
