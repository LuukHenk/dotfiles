from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTreeWidgetItem
from data_models.package import Package

from data_models.dotfile import Dotfile
from data_models.item import Item


class TreeWidgetItem(QTreeWidgetItem):
    __PACKAGE_TEXT = "{installation_message} {name} {version_name} ({manager} | {version_type})"

    def __init__(self, item: Item, parent=None) -> None:
        super().__init__(parent)
        self.setCheckState(0, Qt.Unchecked)
        self.__item = item
        self.__set_text()

    @property
    def item(self) -> Item:
        return self.__item

    def __set_text(self):
        installation_message = "Uninstall" if self.__item.installed else "Install"
        if isinstance(self.__item, Dotfile):
            self.setText(0, f"{installation_message} {self.__item.name}")
        if isinstance(self.__item, Package):
            text = self.__PACKAGE_TEXT.format(
                installation_message=installation_message,
                name=self.__item.name,
                version_name=self.__item.version.name,
                version_type=self.__item.version.type.value,
                manager=self.__item.manager_name.name,
            )
            self.setText(0, text)
