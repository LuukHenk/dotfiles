from typing import List


from installer import Installer
from package_installer.package_finder.data_models.package_info import PackageInfo
from package_installer.package_finder.package_finder import PackageFinder
from package_installer.data_models.package_search_query import PackageSearchQuery

class PackageInstaller(Installer):
    def __init__(self) -> None:
        super().__init__()
        self.__packages_to_install: List[PackageSearchQuery] = [
            PackageSearchQuery(
                name="Neovim",
                search_query=["neovim", "nvim"]
            ),
            PackageSearchQuery(
                name="Spotify",
                search_query=["spotify"]
            )
        ]

        self.__packages = self.__find_packages()
        print(self.__packages)

    
    def install(self) -> bool:
        pass

    def __find_packages(self) -> List[PackageInfo]:
        package_finder = PackageFinder()
        packages: List[PackageInfo] = []
        for package in self.__packages_to_install:
            for package_info in package_finder.find_package(package):
                packages.append(package_info)
        return packages
