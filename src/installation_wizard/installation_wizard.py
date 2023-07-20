from PySide6.QtCore import QObject, Signal
from typing import Dict, List, Callable

from data_layer.package_accessor import PackageAccessor
from data_models.package_old import PackageOld
from installation_wizard.business_layer.id_tracker import IdTracker
from installation_wizard.business_layer.installation_wizard_processor import InstallationWizardProcessor
from installation_wizard.presentation_layer.installation_wizard_widget import InstallationWizardWidget


class InstallationWizard(QObject):
    install = Signal()

    def __init__(self, package_accessor: PackageAccessor, parent=None) -> None:
        super().__init__(parent)
        self.__package_accessor = package_accessor
        self.__installation_wizard_widget = self.__create_installation_wizard_widget()

    @property
    def installation_wizard_widget(self):
        return self.__installation_wizard_widget

    def __create_installation_wizard_widget(self) -> InstallationWizardWidget:
        installation_wizard_processor = InstallationWizardProcessor(self.__package_accessor, IdTracker())
        wizard = InstallationWizardWidget(
            installation_wizard_processor.format_packages_for_installation_wizard(), installation_wizard_processor
        )
        wizard.install.connect(self.__on_installation_request)
        return wizard

    def __on_installation_request(self) -> None:
        self.install.emit()

    def __get_group_data(self) -> Dict[str, List[List[PackageOld]]]:
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
