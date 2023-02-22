
from typing import Optional

from package_installer.manager_enum import Manager
from package_installer.apt_package_manager_mapper import AptPackageManagerMapper
from package_installer.snap_package_manager_mapper import SnapPackageManagerMapper



class PackageHandler:

    def __init__(self) -> None:
        self.__apt_package_manager_mapper = AptPackageManagerMapper()
        self.__snap_package_manager_mapper = SnapPackageManagerMapper()
    
    def check_if_package_exists(package_name: str, package_version: Optional[str]=None, package_manager: Optional[Manager]=None) -> bool:
        """Checks if the given package exists

        Args:
            package_name (str): The name of the package
            package_version (Optional[str], optional): The package version. Defaults to None, where it will try to find the latest version.
            package_manager (Optional[Manager], optional): _description_. Defaults to None, where it will first search in apt packages and otherwise snap.

        Returns:
            bool: True if the package was found
        """
        
    def install_package(package_name: str, package_version: Optional[str]=None, package_manager: Optional[Manager]=None) -> bool:
        """Tries to install a given package
        Args:
            package_name (str): The name of the package to install 
            package_version (Optional[str], optional): The package version. Defaults to None, where it will try to install the latest version.
            package_manager (Optional[Manager], optional): _description_. Defaults to None, where it will first search in apt packages and otherwise snap.

        Returns:
            bool: True if the package was successfully installed
        """
        
    