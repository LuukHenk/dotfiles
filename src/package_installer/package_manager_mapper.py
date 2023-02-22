from typing import List
from abc import ABC, abstractmethod

from package_installer.package import Package
class PackageManagerMapper(ABC):
    
    @abstractmethod
    def map(self, package_name: str) -> List[Package]:
        """Uses the package name to find the package in the package manager and tries to construct it into a 'Package'

        Args:
            package_name (str): The package name to search for

        Returns:
            List[Package]: A list of packages found with the given package name
        """