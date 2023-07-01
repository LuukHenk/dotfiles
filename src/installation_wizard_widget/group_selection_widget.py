from sys import exit as sys_exit, argv

from typing import List, Dict
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
from PySide6.QtCore import Signal


class GroupSelectionWidget(QWidget):
    groupClicked = Signal(str)

    def __init__(self, groups: List[str], parent=None) -> None:
        super().__init__(parent)
        self.__group_tiles: Dict[str, QPushButton] = self.__create_group_tiles(groups)
        self.__create_layout()

    def highlight_groups(self, group_names: List[str]):
        for group_name, tile in self.__group_tiles.items():
            if group_name in group_names:
                tile.setStyleSheet("font-weight: bold;")
            else:
                tile.setStyleSheet("font-weight: normal;")

    def __create_layout(self) -> None:
        layout = QVBoxLayout(self)
        for group in self.__group_tiles.values():
            layout.addWidget(group)
        self.highlight_groups([])

    def __create_group_tiles(self, groups: List[str]) -> Dict[str, QPushButton]:
        group_tiles = {}
        for i, group in enumerate(groups):
            group_tile = self.__create_group_tile(group)
            group_tile.setChecked(i == 0)
            group_tiles[group] = group_tile

        return group_tiles

    def __create_group_tile(self, text: str) -> QPushButton:
        tile = QPushButton(text)
        tile.setCheckable(True)
        tile.clicked.connect(lambda: self.__on_group_clicked(text))
        return tile

    def __on_group_clicked(self, clicked_group_name: str) -> None:
        for group_name, tile in self.__group_tiles.items():
            tile.setChecked(clicked_group_name == group_name)
        self.groupClicked.emit(clicked_group_name)


if __name__ == "__main__":
    app = QApplication(argv)
    window = GroupSelectionWidget(["Nvim", "Python"])
    window.show()
    sys_exit(app.exec())
