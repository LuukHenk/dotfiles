from typing import List

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout

from installation_wizard.presentation_layer.group_button import GroupButton


class GroupsPanel(QWidget):
    groupClicked = Signal(str)

    def __init__(self, group_names: List[str], parent=None):
        super().__init__(parent)
        self.__group_buttons: List[QPushButton] = self.__create_group_buttons(group_names)
        self.__create_layout()

    def highlight_groups(self, group_names: List[str]):
        for group_button in self.__group_buttons:
            if group_button.text() in group_names:
                group_button.setStyleSheet("font-weight: bold;")
            else:
                group_button.setStyleSheet("font-weight: normal;")

    def check_group(self, group_name) -> None:
        self.__on_group_clicked(group_name)

    def __create_layout(self) -> None:
        layout = QVBoxLayout(self)
        for group in self.__group_buttons:
            layout.addWidget(group)

    @Slot(str)
    def __on_group_clicked(self, clicked_group_name: str) -> None:
        for button in self.__group_buttons:
            button.setChecked(clicked_group_name == button.text())
        self.groupClicked.emit(clicked_group_name)

    def __create_group_buttons(self, group_names: List[str]) -> List[GroupButton]:
        return [self.__create_group_button(group_name) for group_name in group_names]

    def __create_group_button(self, group_name: str) -> GroupButton:
        button = GroupButton(group_name)
        button.groupNameClicked.connect(self.__on_group_clicked)
        return button
