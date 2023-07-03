from typing import List, Final

from PySide6.QtCore import Slot, Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel

from data_models.package import Package
from installation_wizard.presentation_layer.package_widget import PackageWidget


class PackagesWidget(QWidget):
    packageStateChange = Signal(int, int)  # Tuple[package ID, package state]
    updatePackageState = Signal(int, int)  # Tuple[package ID, package state]

    def __init__(self, packages: List[Package], parent=None):
        super().__init__(parent=parent)
        self.__package_header_point_size = QFont().pointSize() * 2
        self.__create_layout(packages)

    def __create_layout(self, packages: List[Package]):
        layout = QVBoxLayout(self)
        if not packages:
            return
        layout.addWidget(self.__create_header(packages[0].name))
        for package in packages:
            layout.addWidget(self.__create_package_widget(package))

    def __create_package_widget(self, package: Package) -> PackageWidget:
        package_widget = PackageWidget(package)
        package_widget.stateChanged.connect(lambda state: self.__on_package_clicked(package.id_, state))
        self.updatePackageState.connect(package_widget.updatePackageState)
        return package_widget

    @Slot(int, int)
    def __on_package_clicked(self, package_id: int, package_state: int):
        self.packageStateChange.emit(package_id, package_state)

    def __create_header(self, text: str) -> QLabel:
        header = QLabel(text)
        header.setStyleSheet(f"font-size: {self.__package_header_point_size}; font-weight: bold;")
        return header