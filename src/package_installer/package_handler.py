
from typing import Optional

from package_installer.manager_enum import Manager
from package_installer.package_manager_mappers.package_manager_mapper import PackageManagerMapper
from package_installer.package_manager_mappers.apt_package_manager_mapper import AptPackageManagerMapper
from package_installer.package_manager_mappers.snap_package_manager_mapper import SnapPackageManagerMapper
from package_installer.package import Package


class PackageHandler:

    def __init__(self) -> None:
        self.__apt_package_manager_mapper = AptPackageManagerMapper()
        self.__snap_package_manager_mapper = SnapPackageManagerMapper()
    
    def check_if_package_exists(self, package: Package) -> bool:
        """Checks if the given package exists

        Args:
            package: Package: the package to search for
            
        Returns:
            bool: True if the package was found
        """
        mapper = self.__select_mapper(package.manager)
        mapper.map(package.name)
        
    def install_package(package: Package) -> bool:
        """Tries to install a given package
        Args:
            package: Package: the package to install
            
        Returns:
            bool: True if the package was successfully installed
        """
    
    def __select_mapper(self, manager: Manager) -> PackageManagerMapper:
        if manager == Manager.APT:
            return self.__apt_package_manager_mapper
        elif manager == Manager.SNAP:
            return self.__snap_package_manager_mapper