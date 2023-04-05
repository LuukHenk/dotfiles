
from typing import Dict, List

from data_models.package_info import PackageInfo

from package_finder.package_managers.package_manager_finder import PackageManagerFinder
from package_finder.package_managers.apt_package_manager_finder import AptPackageManagerFinder
from package_finder.package_managers.snap_package_manager_finder import SnapPackageManagerFinder
from package_finder.package_search_request_parser import PackageSearchRequestParser

class PackageFinder:
    def __init__(self) -> None:
        self.__package_managers: List[PackageManagerFinder] = [ # type: ignore
            AptPackageManagerFinder(),
            SnapPackageManagerFinder()
        ]
        self.__package_search_requests = PackageSearchRequestParser().package_search_requests
        
    def get_package_info(self) -> Dict[str, List[PackageInfo]]:
        package_info = {}
        for search_requests in self.__package_search_requests:
            package_group = []
            for manager in self.__package_managers:
                for package_name in search_requests.search_query:
                    package_group += manager.find_package(package_name)
            package_info[search_requests.package_group] = package_group
            
        return package_info
    
