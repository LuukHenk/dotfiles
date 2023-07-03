from typing import Dict, List

from data_layer.package_accessor import PackageAccessor
from data_models.package import Package
from installation_wizard_widget.business_layer.package_id_tracker import PackageIdTracker

from installation_wizard_widget.presentation_layer.installation_wizard_widget import InstallationWizardWidget
from installation_wizard_widget.presentation_layer.stacked_group_panels import StackedGroupPanels


class Factory:
    def __init__(self, package_accessor: PackageAccessor):
        self.__package_accessor = package_accessor
        self.__package_id_tracker = PackageIdTracker()
        self.__installation_wizard_widget = self.__create_installation_wizard_widget()

    @property
    def installation_wizard_widget(self) -> InstallationWizardWidget:
        return self.__installation_wizard_widget

    def __create_installation_wizard_widget(self) -> InstallationWizardWidget:
        sorted_group_names = sorted(self.__package_accessor.get_groups())
        stacked_group_panels = self.__construct_stacked_group_panels()
        return InstallationWizardWidget(sorted_group_names, stacked_group_panels)

    def __construct_stacked_group_panels(self) -> StackedGroupPanels:
        stacked_group_panels = StackedGroupPanels()
        for group_name, package_sets in self.__get_group_data().items():
            stacked_group_panels.add_group_panel(group_name, package_sets)
        return stacked_group_panels

    def __get_group_data(self) -> Dict[str, List[List[Package]]]:
        # TODO: #0000002
        groups = {}
        for group in self.__package_accessor.get_groups():
            package_sets = []
            for package_name in self.__package_accessor.get_package_names():
                package_set = self.__package_accessor.find(name=package_name)
                package_groups = [group for package in package_set for group in package.groups]
                if group in package_groups:
                    package_sets.append(package_set)
            groups[group] = package_sets
        return groups
