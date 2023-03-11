
from typing import List, Final, Optional

from utils.subprocess_interface import run_
from data_models.version import Version
from data_models.manager import Manager
from data_models.package_info import PackageInfo
from package_finder.package_managers.package_manager_finder import PackageManagerFinder

class AptPackageManagerFinder(PackageManagerFinder):
    INFO_COMMAND: Final[List[str]] = ["apt", "info"]
    INSTALLED_COMMAND: Final[List[str]] = ["dpkg-query", "-l"]
    VERSION_INDICATOR: Final[str] = "\nVersion: "
    
    def find_package(self, package_name: str) -> List[PackageInfo]:
        latest_version = self.__find_latest_package_version(package_name)
        installed_version = self.__find_installed_version(package_name)
        return self.__generate_package_info(package_name, latest_version, installed_version)

    
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

    @staticmethod
    def __find_version(command: List[str], version_indicator: str) -> Optional[str]:
        package_info = run_(command)
        if package_info.returncode != 0 or not version_indicator in package_info.stdout:
            return None
        return package_info.stdout.split(version_indicator)[1]
    
    @staticmethod
    def __check_if_latest_package_is_installed(latest_version: Optional[str], installed_version: Optional[str]) -> bool:
        package_installed = False
        if latest_version is not None and installed_version is not None:
            package_installed = latest_version == installed_version
        return package_installed

    def __generate_package_info(
        self,
        package_name:str, 
        latest_version: Optional[str], 
        installed_version: Optional[str]
    ) -> List[PackageInfo]:

        latest_installed = self.__check_if_latest_package_is_installed(
            latest_version=latest_version,
            installed_version=installed_version  
        )
        packages: List[PackageInfo] = []

        if latest_version is not None:
            if latest_installed:
                packages.append(PackageInfo(
                    name=package_name,
                    version=(latest_version, Version.LATEST_STABLE),
                    installed=True,
                    manager=Manager.APT,
                ))
            else:
                packages.append(PackageInfo(
                    name=package_name,
                    version=(latest_version, Version.LATEST_STABLE),
                    installed=False,
                    manager=Manager.APT,
                ))
                    
        if installed_version is not None and not latest_installed:
            packages.append(PackageInfo(
                name=package_name,
                version=(installed_version, Version.OTHER),
                installed=True,
                manager=Manager.APT,
            ))
        
        return packages