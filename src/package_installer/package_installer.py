from typing import List


from installer import Installer
from package_installer.package_handler import PackageHandler
from package_installer.data_models.package_search_query import PackageSearchQuery

class PackageInstaller(Installer):
    def __init__(self) -> None:
        super().__init__()
        self.__packages_to_install: List[PackageSearchQuery] = [
            PackageSearchQuery(
                name="Python3",
                search_query=["python3", "htop"]
            )
        ]
        self.__package_handler: PackageHandler = PackageHandler()
        
        for package in self.__packages_to_install:
            print(self.__package_handler.get_package_info(package))
    
    def install(self) -> bool:
        pass

