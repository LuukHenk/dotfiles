from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTreeWidgetItem
from data_models.package import Package

from data_models.dotfile import Dotfile
from data_models.item import Item
from installation_wizard.business_layer.widget_text_generator import generate_text


class TreeWidgetItem(QTreeWidgetItem):
    __PACKAGE_TEXT = "{installation_message} {name} {version_name} ({manager} | {version_type})"

    def __init__(self, item: Item, parent=None) -> None:
        super().__init__(parent)
        self.setCheckState(0, Qt.Unchecked)
        self.__item = item
        self.setText(0, generate_text(self.__item))

    @property
    def item(self) -> Item:
        return self.__item
