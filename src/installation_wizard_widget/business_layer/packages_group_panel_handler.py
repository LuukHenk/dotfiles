from typing import Dict

from data_layer.package_accessor import PackageAccessor
from installation_wizard_widget.presentation_layer.packages_group_panel import PackagesGroupPanel


class PackagesGroupPanelHandler:
    def __init__(self, package_accessor: PackageAccessor):
        self.__packages_group_panels = self.__construct_panels(package_accessor)

    def get_groups_panel(self, group_name: str) -> PackagesGroupPanel:
        return self.__packages_group_panels[group_name]

    @staticmethod
    def __construct_panels(package_accessor) -> Dict[str, PackagesGroupPanel]:
        # TODO: #0000002
        groups = {}
        for group in package_accessor.get_groups():
            package_sets = []
            for package_name in package_accessor.get_package_names():
                package_set = package_accessor.find(name=package_name)
                package_groups = [group for package in package_set for group in package.groups]
                if group in package_groups:
                    package_sets.append(package_set)
            groups[group] = PackagesGroupPanel(group, package_sets)
        return groups
