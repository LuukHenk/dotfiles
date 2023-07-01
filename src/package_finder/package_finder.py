from typing import Dict, List

from data_models.package_info import PackageInfo
from data_models.package_search_request import ParsedPackage

from package_finder.package_managers.package_manager_finder import PackageManagerFinder
from package_finder.package_managers.apt_package_manager_finder import AptPackageManagerFinder
from package_finder.package_managers.snap_package_manager_finder import SnapPackageManagerFinder


class PackageFinder:
    def __init__(self) -> None:
        self.__package_managers: List[PackageManagerFinder] = [AptPackageManagerFinder(), SnapPackageManagerFinder()]

    def get_packages_info(self, parsed_packages: List[ParsedPackage]) -> List[PackageInfo]:
        packages_info = []
        for parsed_package in parsed_packages:
            for manager in self.__package_managers:
                for search_request in parsed_package.search_query:
                    packages_info += manager.find_package(search_request, parsed_package.package_group)
        return packages_info
