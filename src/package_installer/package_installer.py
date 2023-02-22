from typing import List

from etc.packages_to_install import packages
from installer import Installer
from package_installer.package import Package
from package_installer.package_handler import PackageHandler

class PackageInstaller(Installer):
    def __init__(self) -> None:
        super().__init__()
        self.__packages_to_install: List[Package] = packages
        self.__package_handler: PackageHandler = PackageHandler()
    
    def install(self) -> bool:
        for package in self.__packages_to_install:
            self.__package_handler.check_if_package_exists(package)



