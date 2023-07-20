from typing import List

from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout

from data_models.item import Item
from installation_wizard.data_models.installation_wizard_data_formats import ItemGroupsFormat
from installation_wizard.presentation_layer.group_tree_widget import GroupTreeWidget


class InstallationWizardWidget(QWidget):
    def __init__(self, item_groups: ItemGroupsFormat, parent=None):
        super().__init__(parent)
        self.__apply_button = QPushButton("Apply Changes")
        self.__apply_button.clicked.connect(self.__show_confirmation_widget)
        self.__group_tree_widget = GroupTreeWidget(item_groups)
        self.__create_layout()

    def __create_layout(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.__group_tree_widget)
        layout.addWidget(self.__apply_button)

    def __show_confirmation_widget(self):
        pass
