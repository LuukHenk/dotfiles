from PySide6.QtCore import QObject
from typing import Dict, List, Callable

from data_layer.package_accessor import PackageAccessor
from data_models.package import Package
from installation_wizard.business_layer.id_tracker import IdTracker
from installation_wizard.business_layer.installation_wizard_processor import InstallationWizardProcessor
from installation_wizard.presentation_layer.installation_wizard_widget import InstallationWizardWidget


class InstallationWizard(QObject):
    def __init__(self, package_accessor: PackageAccessor, install_callable: Callable[[], None], parent=None) -> None:
        super().__init__(parent)
        self.__package_accessor = package_accessor
        self.__install_callable = install_callable
        self.__installation_wizard_widget = self.__create_installation_wizard_widget()

    def show(self):
        self.__installation_wizard_widget.show()

    def __create_installation_wizard_widget(self) -> InstallationWizardWidget:
        installation_wizard_processor = InstallationWizardProcessor(self.__package_accessor, IdTracker())
        wizard = InstallationWizardWidget(self.__get_group_data(), installation_wizard_processor)
        wizard.install.connect(self.__on_installation_request)
        return wizard

    def __on_installation_request(self) -> None:
        self.__installation_wizard_widget.hide()
        self.__install_callable()

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