from typing import List


from installer import Installer
from package_installer.package_finder.data_models.package_info import PackageInfo
from package_installer.package_finder.package_finder import PackageFinder
from package_installer.data_models.package_search_query import PackageSearchQuery

class PackageInstaller(Installer):
    def __init__(self) -> None:
        super().__init__()
        self.__packages_search_query =  self.__generate_package_search_query()
        self.__packages = self.__find_packages()
        print(self.__packages)

    
    def install(self) -> bool:
        return False

    def __find_packages(self) -> List[PackageInfo]:
        package_finder = PackageFinder()
        packages: List[PackageInfo] = []
        for package in self.__packages_search_query:
            for package_info in package_finder.find_package(package):
                packages.append(package_info)
        return packages
    
    @staticmethod
    def __generate_package_search_query() -> List[PackageSearchQuery]:
        return [
            PackageSearchQuery(
                name="Neovim",
                search_query=["neovim", "nvim"]
            ),
            PackageSearchQuery(
                name="Spotify",
                search_query=["spotify"]
            )
        ]
