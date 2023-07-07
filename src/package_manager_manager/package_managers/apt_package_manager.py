from subprocess import CompletedProcess, Popen
from typing import List, Final, Optional, Tuple

from data_models.manager_name import ManagerName
from data_models.package import Package
from data_models.result import Result
from data_models.version import Version

from data_models.package_manager_search_result import PackageManagerSearchResult
from data_models.version_type import VersionType
from package_manager_manager.package_managers.package_manager import PackageManager
from package_manager_manager.utils.subprocess_interface import run_, run_async_command


class AptPackageManager(PackageManager):
    __APT = "apt"
    __APT_GET = "apt-get"
    __INFO_COMMAND: Final[List[str]] = [__APT, "info"]
    __INSTALLED_COMMAND: Final[List[str]] = ["dpkg-query", "-l"]
    __VERSION_INDICATOR: Final[str] = "\nVersion: "

    def swap_installation_status(self, package: Package) -> Result:
        installed_text = "remove" if package.installed else "install"
        installation_command = f"{self.__APT_GET} {installed_text} {package.search_name} -y"
        result = run_async_command(installation_command)
        return self._generate_installation_result_message(package, result)

    def find_package(self, package_name: str) -> List[PackageManagerSearchResult]:
        latest_version = self.__find_latest_package_version(package_name)
        installed_version = self.__find_installed_version(package_name)
        return self.__generate_package_manager_search_result(latest_version, installed_version)

    def __find_latest_package_version(self, package_name: str) -> Optional[str]:
        command = self.__INFO_COMMAND + [package_name]
        latest_version = self.__find_version(command, self.__VERSION_INDICATOR)
        if not latest_version:
            return None
        return latest_version.split("\n")[0]

    def __find_installed_version(self, package_name: str) -> Optional[str]:
        command = self.__INSTALLED_COMMAND + [package_name]
        installed_version = self.__find_version(command, package_name)
        if not installed_version:
            return None
        return installed_version.strip().split()[0]

    @staticmethod
    def __find_version(command: List[str], version_indicator: str) -> Optional[str]:
        package_info = run_(command)
        if package_info.returncode != 0 or version_indicator not in package_info.stdout:
            return None
        return package_info.stdout.split(version_indicator)[1]

    @staticmethod
    def __check_if_latest_package_is_installed(latest_version: Optional[str], installed_version: Optional[str]) -> bool:
        package_installed = False
        if latest_version is not None and installed_version is not None:
            package_installed = latest_version == installed_version
        return package_installed

    def __generate_package_manager_search_result(
        self, latest_version: Optional[str], installed_version: Optional[str]
    ) -> List[PackageManagerSearchResult]:
        latest_installed = self.__check_if_latest_package_is_installed(
            latest_version=latest_version, installed_version=installed_version
        )
        packages: List[PackageManagerSearchResult] = []
        if latest_version is not None:
            version = Version(name=latest_version, type=VersionType.LATEST_STABLE)
            packages.append(
                PackageManagerSearchResult(
                    package_version=version, package_installed=latest_installed, manager_name=ManagerName.APT
                )
            )
        if installed_version is not None and not latest_installed:
            version = Version(name=installed_version, type=VersionType.OTHER)
            packages.append(
                PackageManagerSearchResult(
                    package_version=version, package_installed=True, manager_name=ManagerName.APT
                )
            )
        return packages
