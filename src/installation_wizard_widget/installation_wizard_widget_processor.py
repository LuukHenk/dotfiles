from typing import List, Dict
from data_models.package_info import PackageInfo
from package_finder.package_finder import PackageFinder


class InstallationWizardWidgetProcessor:
    def __init__(self) -> None:
        self.__package_info_groups: Dict[str, List[PackageInfo]] = PackageFinder().get_package_info()

    @property
    def package_info_groups(self) -> Dict[str, List[PackageInfo]]:
        return self.__package_info_groups

    def update_installation_request_status(self, package_info: PackageInfo):
        for packages in self.__package_info_groups.values():
            for package in packages:
                if package == package_info:
                    package.installation_request = not package.installation_request

    def install_packages(self) -> None:
        """Installs the packages with an installation request"""
        print(self.__find_packages_with_an_installation_request())


    def __find_packages_with_an_installation_request(self) -> List[PackageInfo]:
        packages_with_installation_request = []
        for packages in self.__package_info_groups.values():
            for package in packages:
                if package.installation_request:
                    packages_with_installation_request.append(package)
        return packages_with_installation_request
