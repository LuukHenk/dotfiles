from PySide6.QtWidgets import QWidget, QHBoxLayout, QPushButton
from PySide6.QtCore import Signal


class ControlsWidget(QWidget):
    InstallClicked = Signal()

    def __init__(self):
        super().__init__()
        self.__create_layout()

    def __create_layout(self) -> None:
        layout = QHBoxLayout(self)
        install_button = QPushButton("Apply changes")
        install_button.clicked.connect(self.InstallClicked)
        layout.addWidget(install_button)
