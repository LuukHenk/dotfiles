
from typing import Dict, List

from data_models.package_info import PackageInfo
from package_finder.package_finder import PackageFinder
class PackageAccessor:
    def __init__(self):
        self.__package_groups = PackageFinder().get_package_info()

    @property
    def package_info_groups(self) -> Dict[str, List[PackageInfo]]:
        return self.__package_groups

    def update_installation_request_status(self, package_info: PackageInfo):
        for packages in self.__package_groups.values():
            for package in packages:
                if package == package_info:
                    package.installation_request = not package.installation_request

    def find_packages_with_an_installation_request(self) -> List[PackageInfo]:
        packages_with_installation_request = []
        for packages in self.__package_groups.values():
            for package in packages:
                if package.installation_request:
                    packages_with_installation_request.append(package)
        return packages_with_installation_request
