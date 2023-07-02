from typing import List, Dict

from PySide6.QtCore import Signal
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel

from data_models.package import Package
from installation_wizard_widget.presentation_layer.packages_widget import PackagesWidget


class PackagesGroupPanel(QWidget):
    packageClicked = Signal(int)

    def __init__(self, group_name: str, package_sets: List[List[Package]], parent=None):
        super().__init__(parent)
        self.__group_point_size = QFont().pointSize() * 3
        self.__create_layout(group_name, package_sets)

    def __create_layout(self, group_name: str, package_sets: List[List[Package]]):
        layout = QHBoxLayout(self)
        layout.addWidget(self.__create_header(group_name))
        for package_set in package_sets:
            packages_widget = PackagesWidget(package_set)
            packages_widget.packageClicked.connect(self.packageClicked)
            layout.addWidget(packages_widget)

    def __create_header(self, text: str) -> QLabel:
        header = QLabel(text)
        header.setStyleSheet(f"font-size: {self.__group_point_size}; font-weight: bold;")
        return header
