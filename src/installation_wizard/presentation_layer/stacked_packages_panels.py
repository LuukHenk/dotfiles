from typing import Dict, List

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QStackedWidget

from data_models.package import Package
from installation_wizard.data_layer.typing_hints import PackageSets
from installation_wizard.presentation_layer.packages_panel import PackagesPanel


class StackedPackagesPanels(QStackedWidget):
    otherPackageChecked = Signal(int, bool)  # Tuple[package ID, package check state]
    packageChecked = Signal(int, bool)  # Tuple[package ID, package check state]

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.__panels: Dict[str, PackagesPanel] = {}

    def add_group_panel(self, group_name, package_sets: PackageSets):
        panel = PackagesPanel(group_name, package_sets)
        panel.packageChecked.connect(self.packageChecked)
        panel.packageChecked.connect(self.otherPackageChecked)
        self.otherPackageChecked.connect(panel.otherPackageChecked)
        self.__panels[group_name] = panel
        self.addWidget(panel)

    def switch_group_panel(self, group_name: str):
        self.setCurrentWidget(self.__panels[group_name])
