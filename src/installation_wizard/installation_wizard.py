from typing import List

from PySide6.QtCore import QObject, Signal, Slot

from data_models.item import Item
from installation_wizard.business_layer.config_formatter import format_by_groups
from installation_wizard.presentation_layer.installation_wizard_widget import InstallationWizardWidget


class InstallationWizard(QObject):
    install = Signal(object)

    def __init__(self, config: List[Item], parent=None) -> None:
        super().__init__(parent)
        self.__installation_wizard_widget = self.__create_installation_wizard_widget(config)

    @property
    def installation_wizard_widget(self):
        return self.__installation_wizard_widget

    def __create_installation_wizard_widget(self, config: List[Item]) -> InstallationWizardWidget:
        config_groups = format_by_groups(config)
        wizard = InstallationWizardWidget(config_groups)
        wizard.install.connect(self.__on_installation_request)
        return wizard

    @Slot(object)
    def __on_installation_request(self, items_to_install: List[Item]) -> None:
        self.install.emit(items_to_install)
