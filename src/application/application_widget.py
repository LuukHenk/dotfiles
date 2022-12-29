

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PySide6.QtCore import Signal

class ApplicationWidget(QWidget):
    onInstall = Signal()
    def __init__(self) -> None:
        super().__init__()

        self.__widgets = QVBoxLayout(self)
        application_widgets = QWidget()
        application_widgets.setLayout(self.__widgets)

        application_layout = QVBoxLayout()
        application_layout.addWidget(application_widgets)
        install_button = QPushButton("Install")
        install_button.clicked.connect(self.onInstall)
        application_layout.addWidget(install_button)
        self.setLayout(application_layout)


    def add_widget(self, widget: QWidget) -> None:
        self.__widgets.addWidget(widget)
        
