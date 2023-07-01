from abc import ABC, abstractmethod
from typing import List

from data_models.package_manager_search_result import PackageManagerSearchResult


class PackageManager(ABC):
    @abstractmethod
    def find_package(self, package_name: str) -> List[PackageManagerSearchResult]:
        pass
