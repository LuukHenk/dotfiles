
from typing import Tuple, List, Dict, Final, Optional
from subprocess import run
from package_installer.package_manager_mappers.package_manager_mapper import PackageManagerMapper
from package_installer.package_info import PackageInfo
from package_installer.version_enum import Version

class SnapPackageManagerMapper(PackageManagerMapper):
    INFO_COMMAND: Final[List[str]] = ["snap", "info"]
    INSTALLED_INDICATOR: Final[str] = "\ninstalled:"
    LATEST_INDICATOR: Final[str] = "latest/"
    TRACKING_INDICATOR: Final[str] = "tracking:"
    STABLE_INDICATOR: Final[str] = "stable"
    CANDIDATE_INDICATOR: Final[str] = "candidate"
    BETA_INDICATOR: Final[str] = "beta"
    EDGE_INDICATOR: Final[str] = "edge"
    
    
        
    def map(self, package_name: str) -> PackageInfo:
        package_info = PackageInfo(name=package_name)
        command = self.INFO_COMMAND + [package_name]
        result = run(command, capture_output=True, encoding="utf-8")
        if result.returncode == 1:
            return package_info
        package_info.found = True

        if not self.__check_if_installed(result.stdout):
            return package_info
        
        package_info.installed = True
        installed_version = self.__find_installed_version(result.stdout)
        if not installed_version:
            print(f"Unable to find installed version of {package_info.name}")
        package_info.installed_version = installed_version
        return package_info
        
    def __check_if_installed(self, snap_info_stdout=str) -> bool:
        return self.INSTALLED_INDICATOR in snap_info_stdout
    
    def __find_installed_version(self,snap_info_stdout=str) -> Optional[Tuple[Version, str]]:
        available_versions = self.__find_available_versions(snap_info_stdout)
        installed_version = snap_info_stdout.split(self.INSTALLED_INDICATOR)[1].split("\n")[0]
        installed_version = self.__format_version(installed_version)
        for version_type, version in available_versions.items():
            if version == installed_version:
                return version_type, version
        return None
        
    def __find_available_versions(self, snap_info_stdout=str) -> Dict[Version, str]:
        channels: Dict[Version, str] = {
            Version.STABLE: "",
            Version.CANDIDATE: "",
            Version.BETA: "",
            Version.EDGE: ""
        }
        for line in snap_info_stdout.splitlines():
            if self.TRACKING_INDICATOR in line or not self.LATEST_INDICATOR in line:
                continue
            version_type, version = line.strip().split(":")
            version = self.__format_version(version)
            if self.STABLE_INDICATOR in version_type:
                channels[Version.STABLE] = version
            elif self.CANDIDATE_INDICATOR in version_type:
                channels[Version.CANDIDATE] = version
            elif self.BETA_INDICATOR in version_type:
                channels[Version.BETA] = version
            elif self.EDGE_INDICATOR in version_type:
                channels[Version.EDGE] = version
        return channels
    
    @staticmethod
    def __format_version(unformatted_version: str) -> str:
        unformatted_version = unformatted_version.strip()
        spacing = " "
        if not spacing in unformatted_version:
            return unformatted_version
        return unformatted_version.split(spacing)[0]