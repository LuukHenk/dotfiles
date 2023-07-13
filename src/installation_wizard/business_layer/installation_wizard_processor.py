from typing import List

from data_layer.package_accessor import PackageAccessor
from data_models.package import Package
from installation_wizard.business_layer.id_tracker import IdTracker


class InstallationWizardProcessor:
    def __init__(self, package_accessor: PackageAccessor, id_tracker: IdTracker):
        self.__package_accessor = package_accessor
        self.__packages_to_install = id_tracker

    def any_selected_packages(self) -> bool:
        return bool(self.__packages_to_install.ids)

    def update_packages_to_install(self, package_id: int, install: bool):
        if install:
            self.__packages_to_install.add_id(package_id)
            return
        self.__packages_to_install.remove_id(package_id)

    def get_packages_to_install(self) -> List[Package]:
        packages = []
        for package_id in self.__packages_to_install.ids:
            packages.append(self.__package_accessor.find_package_via_id(package_id))
        return packages

    def set_installation_requests(self) -> None:
        for package in self.get_packages_to_install():
            package.installation_request = True
            _result = self.__package_accessor.update_package(package.id_, package)

    def format_input_packages(self):
        # TODO: #0000002
        groups = {}
        for group_name in self.__package_accessor.get_groups():
            package_sets = []
            for package_name in self.__package_accessor.get_package_names():
                package_set = self.__package_accessor.find(name=package_name)
                package_groups = [group for package in package_set for group in package.groups]
                if group_name in package_groups:
                    package_sets.append(package_set)
            groups[group_name] = package_sets
        return groups
