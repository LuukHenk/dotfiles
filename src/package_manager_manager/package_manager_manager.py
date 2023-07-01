from typing import Dict, List

from data_models.manager_name import ManagerName
from data_models.package_manager_search_result import PackageManagerSearchResult
from package_manager_manager.package_managers.apt_package_manager import AptPackageManager
from package_manager_manager.package_managers.package_manager import PackageManager
from package_manager_manager.package_managers.snap_package_manager import SnapPackageManager


class PackageManagerManager:
    def __init__(self):
        self.__managers: Dict[ManagerName, PackageManager] = {  # type:ignore
            ManagerName.APT: AptPackageManager(),
            ManagerName.SNAP: SnapPackageManager(),
        }

    def find_package(self, package_name: str) -> List[PackageManagerSearchResult]:
        results = []
        for manager in self.__managers.values():
            results += manager.find_package(package_name)
        return results
