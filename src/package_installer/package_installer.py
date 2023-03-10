from typing import List


from installer import Installer
from package_installer.package_finder.data_models.package_info import PackageInfo
from package_installer.package_finder.package_finder import PackageFinder
from package_installer.data_models.package_search_query import PackageSearchQuery

class PackageInstaller(Installer):
    def __init__(self) -> None:
        super().__init__()
        self.__packages = self.__find_packages()
        print(self.__packages)
        # TODO Generate and display widget

        # TODO Remember the requested installed stuff for the installation

    
    def install(self) -> bool:
        # TODO Fix the installation script
        return False

    def __find_packages(self) -> List[PackageInfo]:
        package_finder = PackageFinder()
        packages: List[PackageInfo] = []
        for search_request in self.__generate_package_search_query():
            for package in package_finder.find_package(search_request):
                packages.append(package)
        return packages
    
    @staticmethod
    def __generate_package_search_query() -> List[PackageSearchQuery]:
        # TODO Create the search query externally
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
