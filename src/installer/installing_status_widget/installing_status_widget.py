from typing import List

from PySide6.QtWidgets import QWidget, QProgressBar, QTextEdit, QVBoxLayout


class InstallationStatusWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__progress_bar = QProgressBar()
        self.__log = QTextEdit()
        self.__log.setReadOnly(True)
        self.__create_layout()

    def update_installation_status(self, percentage_done: int, messages: List[str]):
        self.__log.setText("\n".join(messages))
        self.__progress_bar.setValue(percentage_done)

    def __create_layout(self) -> None:
        layout = QVBoxLayout(self)
        layout.addWidget(self.__progress_bar)
        layout.addWidget(self.__log)
