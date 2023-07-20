from typing import List

from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout

from data_models.item import Item
from installation_wizard.data_models.installation_wizard_data_formats import ItemGroupsFormat
from installation_wizard.presentation_layer.group_tree_widget import GroupTreeWidget


class InstallationWizardWidget(QWidget):
    def __init__(self, item_groups: ItemGroupsFormat, parent=None):
        super().__init__(parent)
        self.__create_layout(item_groups)

    def __create_layout(self, item_groups: ItemGroupsFormat):
        layout = QVBoxLayout(self)
        layout.addWidget(GroupTreeWidget(item_groups))
        layout.addWidget(QPushButton("Apply Changes"))
