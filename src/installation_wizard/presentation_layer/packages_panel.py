from typing import List

from PySide6.QtCore import Signal, Slot
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel

from data_models.package import Package
from installation_wizard.presentation_layer.package_frame import PackageFrame
from stylesheet.data_layer.object_names import PACKAGES_PANEL_HEADER


class PackagesPanel(QWidget):
    otherPackageChecked = Signal(int, bool)  # Tuple[package ID, package check state]
    packageChecked = Signal(int, bool)  # Tuple[package ID, package check state]

    def __init__(self, group_name: str, package_sets: List[List[Package]], parent=None):
        super().__init__(parent)
        self.__create_layout(group_name, package_sets)

    def __create_layout(self, group_name: str, package_sets: List[List[Package]]):
        layout = QHBoxLayout(self)
        layout.addWidget(self.__create_header(group_name))
        for package_set in package_sets:
            if not len(package_set):
                return
            package_frame = PackageFrame(package_set[0].name, package_set)
            package_frame.packageChecked.connect(self.packageChecked)
            self.otherPackageChecked.connect(package_frame.otherPackageChecked)
            layout.addWidget(package_frame)

    @staticmethod
    def __create_header(text: str) -> QLabel:
        header = QLabel(text)
        header.setObjectName(PACKAGES_PANEL_HEADER)
        return header
