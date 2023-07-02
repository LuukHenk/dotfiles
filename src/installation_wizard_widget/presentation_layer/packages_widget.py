from typing import List, Final

from PySide6.QtCore import Slot, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel

from data_models.package import Package
from installation_wizard_widget.presentation_layer.package_widget import PackageWidget


class PackagesWidget(QWidget):
    packageClicked = Signal(int)

    def __init__(self, packages: List[Package], parent=None):
        super().__init__(parent=parent)
        self.__create_layout(packages)
        self.__package_header_point_size = QFont().pointSize() * 2

    def __create_layout(self, packages: List[Package]):
        layout = QVBoxLayout(self)
        if not packages:
            return
        layout.addWidget(self.__create_header(packages[0].name))
        for package in packages:
            layout.addWidget(self.__create_package_widget(package))

    def __create_package_widget(self, package: Package) -> PackageWidget:
        package_widget = PackageWidget(package)
        package_widget.clicked.connect(lambda: self.__on_package_clicked(package.id_))
        return package_widget

    @Slot(int)
    def __on_package_clicked(self, package_id: int):
        self.PackageClicked.emit(package_id)

    def __create_header(self, text: str) -> QLabel:
        header = QLabel(text)
        header.setStyleSheet(f"font-size: {self.__package_header_point_size}; font-weight: bold;")
        return header
