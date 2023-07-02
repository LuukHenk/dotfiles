from typing import Dict

from data_layer.package_accessor import PackageAccessor
from installation_wizard_widget.business_layer.package_id_tracker import PackageIdTracker
from installation_wizard_widget.business_layer.packages_group_panel_handler import PackagesGroupPanelHandler

from installation_wizard_widget.presentation_layer.groups_panel import GroupsPanel
from installation_wizard_widget.presentation_layer.installation_wizard_widget import InstallationWizardWidget
from installation_wizard_widget.presentation_layer.packages_group_panel import PackagesGroupPanel


class Factory:
    def __init__(self, package_accessor: PackageAccessor):
        self.__package_accessor = package_accessor
        self.__package_id_tracker = PackageIdTracker()
        self.__packages_group_panel_handler = PackagesGroupPanelHandler(self.__package_accessor)
        self.__installation_wizard_widget = self.__create_installation_wizard_widget()

    @property
    def installation_wizard_widget(self) -> InstallationWizardWidget:
        return self.__installation_wizard_widget

    def __create_installation_wizard_widget(self) -> InstallationWizardWidget:
        sorted_group_names = sorted(self.__package_accessor.get_groups())
        groups_panel = GroupsPanel(sorted_group_names)
        active_package_group_panel = self.__packages_group_panel_handler.get_active_groups_panel()
        return InstallationWizardWidget(groups_panel, active_package_group_panel)
