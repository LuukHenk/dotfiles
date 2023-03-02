
from typing import List, Final, Optional, Dict

from package_installer.subprocess_interface import run_
from package_installer.data_models.version_enum import Version
from package_installer.data_models.package_info import PackageInfo
from package_installer.data_models.manager_enum import ManagerEnum
from package_installer.package_managers_handlers.package_manager_handler import PackageManagerHandler

class SnapPackageManagerHandler(PackageManagerHandler):
    
    INSTALLED_INDICATOR: Final[str] = "\ninstalled:"
    
    LATEST_INDICATOR: Final[str] = "latest/"
    TRACKING_INDICATOR: Final[str] = "tracking:"

    STABLE_INDICATOR: Final[str] = "latest/stable"
    CANDIDATE_INDICATOR: Final[str] = "latest/candidate"
    BETA_INDICATOR: Final[str] = "latest/beta"
    EDGE_INDICATOR: Final[str] = "latest/edge"
    
    INFO_COMMAND: Final[List[str]] = ["snap", "info"]
    
    def find_package(self, package_name: str) -> List[PackageInfo]:
        latest_versions: Dict[str, Version]  = self.__find_latest_package_versions(package_name)
        installed_version: Optional[str] = self.__find_installed_version(package_name)
        return self.__generate_package_info(package_name, latest_versions, installed_version)

    def __find_latest_package_versions(self, package_name: str) -> Dict[str, Version]:
        package_info = run_(self.INFO_COMMAND + [package_name])
        if package_info.returncode != 0:
            return {}

        latest_versions = {}
        for line in package_info.stdout.splitlines():
            if self.TRACKING_INDICATOR in line or not self.LATEST_INDICATOR in line:
                continue
            version_type, version = line.strip().split(":")
            version = self.__format_version(version)
            if version in latest_versions or version == '^':
                continue
            latest_versions[version] = self.__match_version_type(version_type)
        return latest_versions
    
    def __match_version_type(self, version_type: str) -> Version:
        match version_type:
            case self.STABLE_INDICATOR:
                return Version.LATEST_STABLE
            case self.CANDIDATE_INDICATOR:
                return Version.LATEST_CANDIDATE
            case self.BETA_INDICATOR:
                return Version.LATEST_BETA
            case self.EDGE_INDICATOR:
                return Version.LATEST_EDGE
        return Version.OTHER
    
    def __find_installed_version(self, package_name: str) -> Optional[str]:
        package_info = run_(self.INFO_COMMAND + [package_name])
        if package_info.returncode != 0 or not self.INSTALLED_INDICATOR in package_info.stdout:
            return None
        installed_version = package_info.stdout.split(self.INSTALLED_INDICATOR)[1].split("\n")[0]
        installed_version = self.__format_version(installed_version)
        return installed_version

    @staticmethod
    def __format_version(unformatted_version: str) -> str:
        unformatted_version = unformatted_version.strip()
        spacing = " "
        if not spacing in unformatted_version:
            return unformatted_version
        return unformatted_version.split(spacing)[0]

    @staticmethod
    def __generate_package_info(
        package_name: str, latest_versions: Dict[str, Version], installed_version: Optional[str]
    ) -> List[PackageInfo]:
        
        packages = []
        installed_found = False
        for version in latest_versions:
            installed = False
            if installed_version is not None:
                installed = version == installed_version
                if installed:
                    installed_found = True
            packages.append(PackageInfo(
                name=package_name,
                version=(version, latest_versions[version]),
                installed=installed,
                manager=ManagerEnum.SNAP,
            ))

        if not installed_found and installed_version is not None:
            packages.append(PackageInfo(
                name=package_name,
                version=(installed_version, Version.OTHER),
                installed=True,
                manager=ManagerEnum.SNAP,
            ))     
        
        return packages
