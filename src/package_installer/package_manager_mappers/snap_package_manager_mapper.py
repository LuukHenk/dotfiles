
from typing import Tuple, List, Dict, Final
from subprocess import run
from package_installer.package_manager_mappers.package_manager_mapper import PackageManagerMapper
from package_installer.package_info import PackageInfo
from package_installer.version_enum import Version

class SnapPackageManagerMapper(PackageManagerMapper):
    INFO_COMMAND: Final[List[str]] = ["snap", "info"]
    INSTALLED_INDICATOR: Final[str] = "\ninstalled:"
    LATEST_INDICATOR: Final[str] = "latest/"
    TRACKING_INDICATOR: Final[str] = "tracking:"
    STABLE_INDICATOR: Final[str] = "latest/stable"
    CANDIDATE_INDICATOR: Final[str] = "latest/candidate"
    BETA_INDICATOR: Final[str] = "latest/beta"
    EDGE_INDICATOR: Final[str] = "latest/edge"
    
    
        
    def map(self, package_name: str) -> PackageInfo:
        package_info = PackageInfo(name=package_name)
        
        command = self.INFO_COMMAND + [package_name]
        info_result = run(command, capture_output=True, encoding="utf-8")
        
        if info_result.returncode != 0:
            return package_info
        package_info.found = True

        if not self.__check_if_installed(info_result.stdout):
            return package_info
        package_info.installed = True
        package_info.installed_version = self.__find_installed_version(info_result.stdout)
        
        return package_info
        
    def __check_if_installed(self, snap_info_stdout=str) -> bool:
        return self.INSTALLED_INDICATOR in snap_info_stdout
    
    def __find_installed_version(self,snap_info_stdout=str) -> Tuple[str, Version]:
        available_versions = self.__find_available_versions(snap_info_stdout)
        installed_version = snap_info_stdout.split(self.INSTALLED_INDICATOR)[1].split("\n")[0]
        installed_version = self.__format_version(installed_version)
        for version, version_type in available_versions.items():
            if version == installed_version:
                return version, version_type
        return installed_version, Version.OTHER
        
    def __find_available_versions(self, snap_info_stdout=str) -> Dict[str, Version]:
        channels: Dict[str, Version] = {}
        for line in snap_info_stdout.splitlines():
            if self.TRACKING_INDICATOR in line or not self.LATEST_INDICATOR in line:
                continue
            version_type, version = line.strip().split(":")
            version = self.__format_version(version)
            if version in channels:
                continue
            channels[version] = self.__match_version_type(version_type)
        return channels
    
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
                
            
    @staticmethod
    def __format_version(unformatted_version: str) -> str:
        unformatted_version = unformatted_version.strip()
        spacing = " "
        if not spacing in unformatted_version:
            return unformatted_version
        return unformatted_version.split(spacing)[0]