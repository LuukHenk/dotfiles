
from abc import ABC, abstractmethod
from typing import List

from package_installer.package_finder.data_models.package_info import PackageInfo


class PackageManager(ABC):
    @abstractmethod
    def find_package(self, package_name: str) -> List[PackageInfo]:
        pass