from typing import Dict

from data_layer.package_accessor import PackageAccessor

from installation_wizard_widget.presentation_layer.groups_panel import GroupsPanel
from installation_wizard_widget.presentation_layer.installation_wizard_widget import InstallationWizardWidget
from installation_wizard_widget.presentation_layer.package_group_panel import PackageGroupPanel


class Factory:
    def __init__(self, package_accessor: PackageAccessor):
        self.__package_accessor = package_accessor
        self.__installation_wizard_widget = self.__create_installation_wizard_widget()

    @property
    def installation_wizard_widget(self) -> InstallationWizardWidget:
        return self.__installation_wizard_widget

    def __create_installation_wizard_widget(self) -> InstallationWizardWidget:
        package_group_panels = self.__create_package_group_panels()
        sorted_group_names = sorted(package_group_panels)
        groups_panel = GroupsPanel(sorted_group_names)
        active_package_group_panel = package_group_panels[sorted_group_names[0]]
        return InstallationWizardWidget(groups_panel, active_package_group_panel)

    def __create_package_group_panels(self) -> Dict[str, PackageGroupPanel]:
        return {
            group_name: PackageGroupPanel(group_name, packages)
            for group_name, packages in self.__package_accessor.get_packages_per_group().items()
        }
