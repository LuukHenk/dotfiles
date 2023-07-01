from subprocess import CompletedProcess
from typing import List, Final, Optional, Dict, Tuple

from utils.subprocess_interface import run_
from data_models.version import Version
from data_models.manager import Manager
from data_models.package_info import PackageInfo
from package_finder.package_managers.package_manager_finder import PackageManagerFinder


class SnapPackageManagerFinder(PackageManagerFinder):
    INSTALLED_INDICATOR: Final[str] = "installed:"

    LATEST_INDICATOR: Final[str] = "latest/"
    TRACKING_INDICATOR: Final[str] = "tracking:"

    STABLE_INDICATOR: Final[str] = "latest/stable"
    CANDIDATE_INDICATOR: Final[str] = "latest/candidate"
    BETA_INDICATOR: Final[str] = "latest/beta"
    EDGE_INDICATOR: Final[str] = "latest/edge"

    INFO_COMMAND: Final[List[str]] = ["snap", "info"]

    def __init__(self) -> None:
        self.__active_package_name: str = ""
        self.__active_package_group: str = ""

    def find_package(self, package_name: str, package_group: str) -> List[PackageInfo]:
        self.__active_package_name = package_name
        self.__active_package_group = package_group
        package_info_run_result: CompletedProcess = run_(self.INFO_COMMAND + [package_name])
        if package_info_run_result.returncode != 0:
            return []

        latest_versions: Dict[str, Version] = self.__find_latest_package_versions(package_info_run_result.stdout)
        installed_version: Optional[str] = self.__find_installed_version(package_info_run_result.stdout)
        return self.__generate_package_info(latest_versions, installed_version)

    def __find_latest_package_versions(self, package_info: str) -> Dict[str, Version]:
        latest_versions = {}
        for line in package_info.splitlines():
            if self.TRACKING_INDICATOR in line or self.LATEST_INDICATOR not in line:
                continue
            version_type, version = line.strip().split(":")
            version = self.__format_version(version)
            if version in latest_versions or version == "^":
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

    def __find_installed_version(self, package_info: str) -> Optional[str]:
        if self.INSTALLED_INDICATOR not in package_info:
            return None
        installed_version = package_info.split(self.INSTALLED_INDICATOR)[1]
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
        self, latest_versions: Dict[str, Version], installed_version: Optional[str]
    ) -> List[PackageInfo]:
        packages = []

        if installed_version is None:
            for version_key in latest_versions:
                version = (version_key, latest_versions[version_key])
                packages.append(self.__create_package_info_object(version, installed=False))
        else:
            installed_found_in_latest_versions = False

            for version_key in latest_versions:
                installed = version_key == installed_version
                version = (version_key, latest_versions[version_key])
                packages.append(self.__create_package_info_object(version, installed))

                if installed:
                    installed_found_in_latest_versions = True

            if not installed_found_in_latest_versions:
                version = (installed_version, Version.OTHER)
                packages.append(self.__create_package_info_object(version, installed=True))

        return packages

    def __create_package_info_object(self, version: Tuple[str, Version], installed: bool) -> PackageInfo:
        return PackageInfo(
            name=self.__active_package_name,
            version=version,
            installed=installed,
            manager=Manager.SNAP,
            group=self.__active_package_group,
        )
