from abc import ABC, abstractmethod
from typing import List

from old.data_models.package_info import PackageInfo


class PackageFinder(ABC):
    @abstractmethod
    def find_package(self, package_name: str, package_group: str) -> List[PackageInfo]:
        pass