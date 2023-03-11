
from abc import ABC, abstractmethod
from typing import List

from data_models.package_info import PackageInfo


class PackageManagerFinder(ABC):
    @abstractmethod
    def find_package(self, package_name: str) -> List[PackageInfo]:
        pass