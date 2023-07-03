from abc import ABC, abstractmethod
from typing import List

from data_models.package import Package
from data_models.package_manager_search_result import PackageManagerSearchResult
from data_models.result import Result


class PackageManager(ABC):
    @abstractmethod
    def find_package(self, package_name: str) -> List[PackageManagerSearchResult]:
        pass

    @abstractmethod
    def install_package(self, package: Package) -> Result:
        pass
