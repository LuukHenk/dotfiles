from typing import List, Dict

from data_layer.package_accessor import PackageAccessor

from data_models.package import Package
from installation_wizard_widget.presentation_layer.packages_group_panel import PackagesGroupPanel


class PackagesGroupPanelHandler:
    def __init__(self, package_accessor: PackageAccessor):
        packages = package_accessor.packages
        package_sets: Dict[str, List[Package]] = {}
        for package_name in package_accessor.get_package_names():
            package_sets[package_name] = [package for package in packages if package.name == package_name]
        #
        # for group in package_accessor.get_groups():
        #     [package_sets[package.name] for package in packages if group in package.groups]
        #     PackagesGroupPanel(group, packages)

    def get_active_groups_panel(self) -> PackagesGroupPanel:
        return PackagesGroupPanel("Dummy", [[], []])
