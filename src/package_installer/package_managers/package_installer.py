from abc import ABC, abstractmethod
from typing import Tuple
from data_models.package_info import PackageInfo


class PackageInstaller(ABC):

    @abstractmethod
    def swap_installation_status(self, package: PackageInfo) -> Tuple[bool, str]:
        """Swaps the installation status of the package;
        E.G. if the package status is installed, it will be uninstalled, and visa-versa.

        Returns True if the swapping was successful; False with an error message if not.
        """
