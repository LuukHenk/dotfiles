from typing import Dict, List

from data_models.package_info import PackageInfo
from data_models.parsed_package import ParsedPackage

from package_finder.package_managers.package_finder import PackageFinder
from package_finder.package_managers.apt_package_finder import AptPackageFinder
from package_finder.package_managers.snap_package_finder import SnapPackageFinder


class PackagesFinder:
    def __init__(self) -> None:
        self.__package_managers: List[PackageFinder] = [AptPackageFinder(), SnapPackageFinder()]

    def get_packages_info(self, parsed_packages: List[ParsedPackage]) -> List[PackageInfo]:
        packages_info = []
        for parsed_package in parsed_packages:
            for manager in self.__package_managers:
                for search_request in parsed_package.search_query:
                    packages_info += manager.find_package(search_request, parsed_package.package_group)
        return packages_info
