
from typing import List
from package_installer.data_models.package_info import PackageInfo
from package_installer.data_models.package_search_query import PackageSearchQuery

from package_installer.package_managers_handlers.package_manager_handler import PackageManagerHandler
from package_installer.package_managers_handlers.apt_package_manager_handler import AptPackageManagerHandler
from package_installer.package_managers_handlers.snap_package_manager_handler import SnapPackageManagerHandler

class PackageHandler:
    def __init__(self) -> None:
        self.__package_managers: List[PackageManagerHandler] = [
            AptPackageManagerHandler(),
            SnapPackageManagerHandler()
        ]
        
    def get_package_info(self, package: PackageSearchQuery) -> List[PackageInfo]:
        package_info = []
        for manager in self.__package_managers:
            for package_name in package.search_query:
                package_info += manager.find_package(package_name)
            
        return package_info
    
