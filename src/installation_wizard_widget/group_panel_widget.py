from sys import exit as sys_exit, argv

from typing import List
from PySide6.QtWidgets import (
    QWidget, 
    QApplication, 
    QVBoxLayout,
    QPushButton
)
from PySide6.QtCore import Signal

class GroupPanelWidget(QWidget):

    groupClicked = Signal(str)
    
    def __init__(self, groups: List[str], parent=None) -> None:
        super().__init__(parent)
        self.__create_layout(groups)

    def __create_layout(self, groups: List[str]) -> None:
        layout = QVBoxLayout(self)
        for group in groups:
            layout.addWidget(self.__create_group_tile(group))

    def __create_group_tile(self, text: str) -> QPushButton:
        tile = QPushButton(text)
        tile.clicked.connect(lambda: self.__on_group_clicked(text))
        return tile
    
    def __on_group_clicked(self, group_name: str) -> None:
        self.groupClicked.emit(group_name)
        
if __name__ == "__main__":
    app = QApplication(argv)
    window = GroupPanelWidget(["Nvim", "Python"])
    window.show()
    sys_exit(app.exec())
