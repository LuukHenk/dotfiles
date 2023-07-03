from typing import Final

from PySide6.QtCore import Signal, Qt, Slot
from PySide6.QtWidgets import QCheckBox

from data_models.package import Package
from installation_wizard_widget.business_layer.package_info_text_generator import generate_package_text


class PackageWidget(QCheckBox):
    updatePackageState = Signal(int, int)  # Tuple[package ID, package state]

    def __init__(self, package: Package, parent=None):
        self.__id = package.id_
        package_text = generate_package_text(package)
        super().__init__(package_text, parent=parent)
        self.updatePackageState.connect(self.__on_package_state_changed)

    @Slot(int, int)
    def __on_package_state_changed(self, package_id: int, package_state: int):
        if package_id != self.__id:
            return
        self.blockSignals(True)
        self.setCheckState(Qt.CheckState(package_state))
        self.blockSignals(False)
