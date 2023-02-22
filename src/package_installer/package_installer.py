from typing import List

from etc.packages_to_install import packages
from installer import Installer
from package_installer.package_to_install import PackageToInstall

class PackageInstaller(Installer):
    def __init__(self) -> None:
        super().__init__()
        self.__packages_to_install: List[PackageToInstall] = packages
    
    def install(self) -> bool:
        for package in self.__packages_to_install:
            print(package.possible_package_names)



