from subprocess import CompletedProcess
from typing import List, Final, Dict, Optional

from data_models.manager_name import ManagerName
from data_models.package import Package
from data_models.result import Result
from data_models.version import Version
from utils.subprocess_interface import run_

from data_models.package_manager_search_result import PackageManagerSearchResult
from data_models.version_type import VersionType
from package_manager_manager.package_managers.package_manager import PackageManager


class SnapPackageManager(PackageManager):
    __INSTALLED_INDICATOR: Final[str] = "installed:"

    __LATEST_INDICATOR: Final[str] = "latest/"
    __TRACKING_INDICATOR: Final[str] = "tracking:"

    __STABLE_INDICATOR: Final[str] = "latest/stable"
    __CANDIDATE_INDICATOR: Final[str] = "latest/candidate"
    __BETA_INDICATOR: Final[str] = "latest/beta"
    __EDGE_INDICATOR: Final[str] = "latest/edge"

    __INFO_COMMAND: Final[List[str]] = ["snap", "info"]

    def swap_installation_status(self, package: Package) -> Result:
        return Result(success=False, message=f"Failed to install package {package.name}. Installation not implemented")

    def find_package(self, package_name: str) -> List[PackageManagerSearchResult]:
        package_info_run_result: CompletedProcess = run_(self.__INFO_COMMAND + [package_name])
        if package_info_run_result.returncode != 0:
            return []

        latest_versions: List[Version] = self.__find_latest_package_versions(package_info_run_result.stdout)
        installed_version: Optional[str] = self.__find_installed_version(package_info_run_result.stdout)
        return self.__generate_package_info(latest_versions, installed_version)

    def __find_latest_package_versions(self, package_info: str) -> List[Version]:
        latest_versions = []
        for line in package_info.splitlines():
            if self.__TRACKING_INDICATOR in line or self.__LATEST_INDICATOR not in line:
                continue
            version_type, version = line.strip().split(":")
            version = self.__format_version(version)
            if version in latest_versions or version == "^":
                continue
            latest_versions.append(Version(type=self.__match_version_type(version_type), name=version))
        return latest_versions

    def __match_version_type(self, version_type: str) -> VersionType:
        match version_type:
            case self.__STABLE_INDICATOR:
                return VersionType.LATEST_STABLE
            case self.__CANDIDATE_INDICATOR:
                return VersionType.LATEST_CANDIDATE
            case self.__BETA_INDICATOR:
                return VersionType.LATEST_BETA
            case self.__EDGE_INDICATOR:
                return VersionType.LATEST_EDGE
        return VersionType.OTHER

    def __find_installed_version(self, package_info: str) -> Optional[str]:
        if self.__INSTALLED_INDICATOR not in package_info:
            return None
        installed_version = package_info.split(self.__INSTALLED_INDICATOR)[1]
        installed_version = self.__format_version(installed_version)
        return installed_version

    @staticmethod
    def __format_version(unformatted_version: str) -> str:
        unformatted_version = unformatted_version.strip()
        spacing = " "
        if spacing not in unformatted_version:
            return unformatted_version
        return unformatted_version.split(spacing)[0]

    def __generate_package_info(
        self, latest_versions: List[Version], installed_version: Optional[str]
    ) -> List[PackageManagerSearchResult]:
        search_results = []

        if installed_version is None:
            for version in latest_versions:
                search_results.append(self.__create_search_result(version, installed=False))
            return search_results

        installed_found_in_latest_versions = False

        for version in latest_versions:
            installed = version.name == installed_version
            search_results.append(self.__create_search_result(version, installed))

            if installed:
                installed_found_in_latest_versions = True

        if not installed_found_in_latest_versions:
            version = Version(type=VersionType.OTHER, name=installed_version)
            search_results.append(self.__create_search_result(version, installed=True))

        return search_results

    @staticmethod
    def __create_search_result(version: Version, installed: bool) -> PackageManagerSearchResult:
        return PackageManagerSearchResult(
            package_version=version,
            package_installed=installed,
            manager_name=ManagerName.SNAP,
        )
