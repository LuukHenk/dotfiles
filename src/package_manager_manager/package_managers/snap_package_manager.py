from typing import List

from data_models.package_manager_search_result import PackageManagerSearchResult
from package_manager_manager.package_managers.package_manager import PackageManager


class SnapPackageManager(PackageManager):
    def find_package(self, package_name: str) -> List[PackageManagerSearchResult]:
        return []
