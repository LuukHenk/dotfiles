
from abc import ABC, abstractmethod
from typing import List

from package_installer.data_models.package_info import PackageInfo


class PackageManagerHandler(ABC):
    @abstractmethod
    def find_package(self, package_name: str) -> List[PackageInfo]:
        pass