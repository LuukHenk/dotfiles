

from PySide6.QtWidgets import QWidget, QVBoxLayout


class ApplicationWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.__widgets = QVBoxLayout(self)
        self.setLayout(self.__widgets)

    def add_widget(self, widget: QWidget) -> None:
        self.__widgets.addWidget(widget)
        
