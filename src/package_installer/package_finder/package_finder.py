
from typing import List

from package_installer.data_models.package_search_query import PackageSearchQuery

from package_installer.package_finder.data_models.package_info import PackageInfo
from package_installer.package_finder.package_managers.package_manager import PackageManager
from package_installer.package_finder.package_managers.apt_package_manager import AptPackageManager
from package_installer.package_finder.package_managers.snap_package_manager import SnapPackageManager

class PackageFinder:
    def __init__(self) -> None:
        self.__package_managers: List[PackageManager] = [ # type: ignore
            AptPackageManager(),
            SnapPackageManager()
        ]
        
    def find_package(self, package: PackageSearchQuery) -> List[PackageInfo]:
        package_info = []
        for manager in self.__package_managers:
            for package_name in package.search_query:
                package_info += manager.find_package(package_name)
            
        return package_info
    
