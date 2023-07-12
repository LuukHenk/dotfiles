from typing import Dict, List

from PySide6.QtCore import Signal
from PySide6.QtWidgets import QStackedWidget

from data_models.package import Package

# from installation_wizard.presentation_layer.packages_group_panel import PackagesGroupPanel


class StackedGroupPanels(QStackedWidget):
    packageStateChange = Signal(int, int)  # Tuple[package ID, package state]
    updatePackageState = Signal(int, int)  # Tuple[package ID, package state]

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.__groups: Dict[str, ...] = {}

    def add_group_panel(self):
        pass

    # def add_group_panel(self, group_name, package_sets: List[List[Package]]):
    #     group_panel = PackagesGroupPanel(group_name, package_sets)
    #     group_panel.packageStateChange.connect(self.packageStateChange)
    #     group_panel.packageStateChange.connect(self.updatePackageState)
    #     self.updatePackageState.connect(group_panel.updatePackageState)
    #     self.__groups[group_name] = group_panel
    #     self.addWidget(group_panel)

    def switch_group_panel(self, group_name: str):
        self.setCurrentWidget(self.__groups[group_name])
