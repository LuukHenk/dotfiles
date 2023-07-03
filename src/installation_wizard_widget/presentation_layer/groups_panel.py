from typing import List

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout


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

    def __create_layout(self) -> None:
        layout = QVBoxLayout(self)
        for group in self.__group_buttons:
            layout.addWidget(group)

    @Slot(str)
    def __on_group_clicked(self, clicked_group_name: str) -> None:
        for button in self.__group_buttons:
            button.setChecked(clicked_group_name == button.text())
        self.groupClicked.emit(clicked_group_name)

    def __create_group_buttons(self, group_names: List[str]) -> List[QPushButton]:
        group_buttons = []
        for group_name in group_names:
            button = QPushButton(group_name)
            button.setCheckable(True)
            button.clicked.connect(lambda: self.__on_group_clicked(group_name))
            group_buttons.append(button)
        return group_buttons
