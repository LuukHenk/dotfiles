
from typing import List, Final, Tuple
from subprocess import run
from package_installer.package_manager_mappers.package_manager_mapper import PackageManagerMapper
from package_installer.package_info import PackageInfo
from package_installer.version_enum import Version

class AptPackageManagerMapper(PackageManagerMapper):
    INFO_COMMAND: Final[List[str]] = ["apt", "info"]
    INSTALLED_COMMAND: Final[List[str]] = ["dpkg-query", "-l"]
    VERSION_INDICATOR: Final[str] = "\nVersion: "
    
    def map(self, package_name: str) -> PackageInfo:
        package_info = PackageInfo(name=package_name)
    
        info_command = self.INFO_COMMAND + [package_name]
        info_result = run(info_command, capture_output=True, encoding="utf-8")
        
        if info_result.returncode != 0:
            return package_info
        package_info.found = True
        
        installed_command = self.INSTALLED_COMMAND + [package_name]
        installed_result = run(installed_command, capture_output=True, encoding="utf-8")
        if not installed_result.returncode == 0:
            return package_info
        package_info.installed = True
        package_info.installed_version = self.__find_installed_version(
            package_name,
            info_result.stdout,
            installed_result.stdout
        )
        
        return package_info

    def __find_installed_version(
        self, package_name: str, info_output:str, installed_version_output:str
    ) ->  Tuple[str, Version]:
        installed_version = installed_version_output.split(package_name)[1].strip().split()[0]
        latest_version = info_output.split(self.VERSION_INDICATOR)[1].split("\n")[0]
        if installed_version == latest_version:
            return installed_version, Version.LATEST_STABLE
        return installed_version, Version.OTHER