
from typing import List

from data_models.package_info import PackageInfo

from package_finder.package_managers.package_manager_finder import PackageManagerFinder
from package_finder.package_managers.apt_package_manager_finder import AptPackageManagerFinder
from package_finder.package_managers.snap_package_manager_finder import SnapPackageManagerFinder
from package_finder.package_search_request_parser import get_package_search_requests

class PackageFinder:
    def __init__(self) -> None:
        self.__package_managers: List[PackageManagerFinder] = [ # type: ignore
            AptPackageManagerFinder(),
            SnapPackageManagerFinder()
        ]
        
    def get_package_info(self) -> List[PackageInfo]:
        package_info = []
        for manager in self.__package_managers:
            for search_requests in get_package_search_requests():
                for package_name in search_requests.search_query:
                    package_info += manager.find_package(package_name)
            
        return package_info
    
