from typing import List

from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout


class GroupsPanel(QWidget):
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

    @staticmethod
    def __create_group_buttons(group_names: List[str]) -> List[QPushButton]:
        group_buttons = [QPushButton(group_name) for group_name in group_names]
        group_buttons[0].setChecked(True)
        return group_buttons
