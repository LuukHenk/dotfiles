from typing import Dict, List

from data_models.package_info import PackageInfo
from data_models.package_search_request import PackageSearchRequest

from package_finder.package_managers.package_manager_finder import PackageManagerFinder
from package_finder.package_managers.apt_package_manager_finder import AptPackageManagerFinder
from package_finder.package_managers.snap_package_manager_finder import SnapPackageManagerFinder
from package_finder.package_search_request_parser import PackageSearchRequestParser


class PackageFinder:
    def __init__(self) -> None:
        self.__package_managers: List[PackageManagerFinder] = [AptPackageManagerFinder(), SnapPackageManagerFinder()]
        self.__package_search_requests = PackageSearchRequestParser().package_search_requests

    def get_package_info(self) -> Dict[str, List[PackageInfo]]:
        package_info = {}
        for search_requests in self.__package_search_requests:
            package_group = []
            for manager in self.__package_managers:
                for package_name in search_requests.search_query:
                    package_group += manager.find_package(package_name, search_requests.package_group)
            package_info[search_requests.package_group] = package_group

        return package_info

    def _get_package_info(self, search_requests: List[PackageSearchRequest]) -> List[PackageInfo]:
        packages_info = []
        for search_request in search_requests:
            for manager in self.__package_managers:
                for package_identifier in search_request.search_query:
                    packages = manager.find_package(package_identifier, search_request.package_group)
