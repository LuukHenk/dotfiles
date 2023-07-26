from typing import List

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout

from installation_wizard.data_models.installation_wizard_data_formats import ItemGroupsFormat
from installation_wizard.presentation_layer.confirmation_widget import ConfirmationWidget
from installation_wizard.presentation_layer.group_tree_widget import GroupTreeWidget


class InstallationWizardWidget(QWidget):
    install = Signal(object)  # List[Item]
    __INSTALLATION_APPROVED_ID = 16384

    def __init__(self, item_groups: ItemGroupsFormat, parent=None):
        super().__init__(parent)
        self.__apply_button = QPushButton("Apply Changes")
        self.__apply_button.setEnabled(False)
        self.__apply_button.clicked.connect(self.__show_confirmation_widget)
        self.__group_tree_widget = GroupTreeWidget(item_groups)
        self.__group_tree_widget.checkedItemsChanged.connect(self.__enable_apply_button)
        self.__create_layout()

    def __create_layout(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.__group_tree_widget)
        layout.addWidget(self.__apply_button)

    def __show_confirmation_widget(self):
        confirmation_widget = ConfirmationWidget(self.__group_tree_widget.checked_items)
        install_packages = confirmation_widget.exec()
        if install_packages == self.__INSTALLATION_APPROVED_ID:
            self.setDisabled(True)
            self.install.emit(self.__group_tree_widget.checked_items)

    @Slot(bool)
    def __enable_apply_button(self, enabled: bool):
        self.__apply_button.setEnabled(enabled)
