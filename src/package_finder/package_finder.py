from typing import Dict, List

from data_models.package_info import PackageInfo
from data_models.package_search_request import PackageSearchRequest

from package_finder.package_managers.package_manager_finder import PackageManagerFinder
from package_finder.package_managers.apt_package_manager_finder import AptPackageManagerFinder
from package_finder.package_managers.snap_package_manager_finder import SnapPackageManagerFinder


class PackageFinder:
    def __init__(self) -> None:
        self.__package_managers: List[PackageManagerFinder] = [AptPackageManagerFinder(), SnapPackageManagerFinder()]

    def _get_packages_info(self, search_requests: List[PackageSearchRequest]) -> Dict[str, List[PackageInfo]]:
        package_info = {}
        for search_request in search_requests:
            package_group = []
            for manager in self.__package_managers:
                for package_name in search_request.search_query:
                    package_group += manager.find_package(package_name, search_request.package_group)
            package_info[search_request.package_group] = package_group
        return package_info

    def get_packages_info(self, search_requests: List[PackageSearchRequest]) -> List[PackageInfo]:
        packages_info = []
        for search_request in search_requests:
            for manager in self.__package_managers:
                for package_identifier in search_request.search_query:
                    packages_info += manager.find_package(package_identifier, search_request.package_group)
        return packages_info
