from PySide6.QtWidgets import QWidget, QProgressBar, QTextEdit, QVBoxLayout


class InstallationStatusWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__progress_bar = QProgressBar()
        self.__log = QTextEdit()
        self.__log.setReadOnly(True)
        self.__create_layout()

    def add_message(self, message: str) -> None:
        self.__log.append(message)

    def update_progress_bar(self, value: int):
        self.__progress_bar.setValue(value)

    def __create_layout(self) -> None:
        layout = QVBoxLayout(self)
        layout.addWidget(self.__progress_bar)
        layout.addWidget(self.__log)
