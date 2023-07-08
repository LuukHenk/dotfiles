from typing import List

from PySide6.QtCore import Signal, Slot
from PySide6.QtGui import QPaintEvent, QPainter
from PySide6.QtWidgets import QFrame, QVBoxLayout, QLabel, QSizePolicy, QSpacerItem, QStyleOption, QApplication, QStyle

from data_models.package import Package
from installation_wizard.presentation_layer.designed_package_widget.package_widget import PackageWidget
from stylesheet.data_layer.object_names import PACKAGE_NAME_SET_HEADER, PACKAGE_NAME_SET


class PackageNameSet(QFrame):
    otherPackageChecked = Signal(int, bool)  # Tuple[package ID, package check state]
    packageChecked = Signal(int, bool)  # Tuple[package ID, package check state]

    def __init__(self, package_name: str, packages: List[Package], parent=None):
        super().__init__(parent=parent)
        self.setObjectName(PACKAGE_NAME_SET)
        self.__create_layout(package_name, packages)

    def __create_layout(self, package_name: str, packages: List[Package]):
        layout = QVBoxLayout(self)
        layout.addWidget(self.__create_header(package_name))
        for package in packages:
            layout.addWidget(self.__create_package_widget(package))
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.Fixed, QSizePolicy.MinimumExpanding))

    def __create_package_widget(self, package: Package) -> PackageWidget:
        package_widget = PackageWidget(package)
        package_widget.packageChecked.connect(lambda state: self.__on_package_clicked(package.id_, state))
        self.otherPackageChecked.connect(package_widget.otherPackageChecked)
        return package_widget

    @Slot(int, int)
    def __on_package_clicked(self, package_id: int, package_state: int):
        self.packageChecked.emit(package_id, package_state)

    @staticmethod
    def __create_header(text: str) -> QLabel:
        header = QLabel(text)
        header.setObjectName(PACKAGE_NAME_SET_HEADER)
        return header
