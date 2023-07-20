from typing import List

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget, QGridLayout, QLabel, QSpacerItem, QSizePolicy

from data_models.package_old import PackageOld
from installation_wizard.data_layer.typing_hints import PackageSets
from installation_wizard.presentation_layer.package_frame import PackageFrame
from stylesheet.data_layer.object_names import PACKAGES_PANEL_HEADER


class PackagesPanel(QWidget):
    otherPackageChecked = Signal(int, bool)  # Tuple[package ID, package check state]
    packageChecked = Signal(int, bool)  # Tuple[package ID, package check state]

    __PACKAGE_FRAMES_PER_ROW = 6

    def __init__(self, group_name: str, package_sets: PackageSets, parent=None):
        super().__init__(parent)
        self.__create_layout(group_name, package_sets)

    def __create_layout(self, group_name: str, package_sets: PackageSets):
        layout = QGridLayout(self)
        layout.addWidget(self.__create_header(group_name), 0, 0, 1, self.__PACKAGE_FRAMES_PER_ROW)

        row_idx = 1
        for i, package_name in enumerate(sorted(package_sets.keys())):
            package_set = package_sets[package_name]
            if not len(package_set):
                return
            col_idx = i % self.__PACKAGE_FRAMES_PER_ROW
            layout.addWidget(self.__create_package_frame(package_set), row_idx, col_idx)
            if col_idx + 1 == self.__PACKAGE_FRAMES_PER_ROW:
                layout.addItem(QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Fixed), row_idx, col_idx + 1)
                row_idx += 1
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Fixed, QSizePolicy.MinimumExpanding), row_idx + 1, 0)

    def __create_package_frame(self, package_set: List[PackageOld]) -> PackageFrame:
        package_frame = PackageFrame(package_set[0].name, package_set)
        package_frame.packageChecked.connect(self.packageChecked)
        self.otherPackageChecked.connect(package_frame.otherPackageChecked)
        return package_frame

    @staticmethod
    def __create_header(text: str) -> QLabel:
        header = QLabel(text)
        header.setObjectName(PACKAGES_PANEL_HEADER)
        return header
