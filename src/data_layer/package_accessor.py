from typing import Dict, List

from data_models.package_info import PackageInfo
from package_finder.packages_finder import PackagesFinder


class PackageAccessor:
    def __init__(self, packages_info: List[PackageInfo]):
        self.__packages_info = packages_info

    def get_package_group_names(self) -> List[str]:
        package_groups = []
        for package in self.__packages_info:
            if package.group not in package_groups:
                package_groups.append(package.group)
        return package_groups

    def get_packages_in_group(self, group: str) -> List[PackageInfo]:
        packages = []
        for package in self.__packages_info:
            if package.group == group:
                packages.append(package)
        return packages

    @property
    def package_info_groups(self) -> Dict[str, List[PackageInfo]]:
        return self.__package_groups

    def update_installation_request_status(self, package: PackageInfo):
        for package_info in self.__packages_info:
            if package == package_info:
                package_info.installation_request = not package_info.installation_request

    def any_installation_request(self) -> bool:
        for package in self.__packages_info:
            if package.installation_request:
                return True
        return False

    def find_package_groups_with_an_installation_request(self) -> List[str]:
        package_groups_with_installation_request = []
        for package_info in self.__packages_info:
            if package_info.installation_request and package_info.group not in package_groups_with_installation_request:
                package_groups_with_installation_request.append(package_info.group)
        return package_groups_with_installation_request

    def find_packages_with_an_installation_request(self) -> List[PackageInfo]:
        packages_with_installation_request = []
        for package_info in self.__packages_info:
            if package_info.installation_request:
                packages_with_installation_request.append(package_info)
        return packages_with_installation_request
