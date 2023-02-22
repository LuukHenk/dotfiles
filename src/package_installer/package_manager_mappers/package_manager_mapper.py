from typing import List
from abc import ABC, abstractmethod

from package_installer.package_info import PackageInfo
class PackageManagerMapper(ABC):
    
    @abstractmethod
    def map(self, package_name: str) -> List[PackageInfo]:
        """Uses the package name to find the package in the package manager and tries to construct it into a 'Package'

        Args:
            package_name (str): The package name to search for

        Returns:
            List[PackageInfo]: Info about the given package name
        """