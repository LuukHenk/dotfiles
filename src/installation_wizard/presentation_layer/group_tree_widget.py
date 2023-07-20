from typing import List

from PySide6.QtCore import Slot, Qt, Signal
from PySide6.QtWidgets import QTreeWidget, QTreeWidgetItem

from data_models.item import Item
from installation_wizard.data_models.installation_wizard_data_formats import ItemGroupsFormat
from installation_wizard.presentation_layer.tree_widget_item import TreeWidgetItem


class GroupTreeWidget(QTreeWidget):
    checkedItemsChanged = Signal(bool)

    def __init__(self, item_groups: ItemGroupsFormat, parent=None):
        super().__init__(parent)
        self.setHeaderLabel("Groups")
        self.__add_all_items(item_groups)
        self.itemChanged.connect(self.__update_checked_items)
        self.__checked_items: List[Item] = []

    @property
    def checked_items(self) -> List[Item]:
        return self.__checked_items

    def __add_all_items(self, item_groups: ItemGroupsFormat) -> None:
        for group_name in sorted(list(item_groups.keys())):
            tree_group_item = QTreeWidgetItem()
            tree_group_item.setText(0, group_name)
            for item in item_groups[group_name]:
                tree_widget_item = TreeWidgetItem(item)
                tree_group_item.addChild(tree_widget_item)
            self.addTopLevelItem(tree_group_item)

    @Slot(QTreeWidgetItem)
    def __update_checked_items(self, item_widget: QTreeWidgetItem) -> None:
        item = item_widget.item
        if item_widget.checkState(0) == Qt.Checked and item not in self.__checked_items:
            self.__checked_items.append(item)
        elif item_widget.checkState(0) == Qt.Unchecked and item in self.__checked_items:
            self.__checked_items.remove(item)
        self.checkedItemsChanged.emit(bool(self.__checked_items))
