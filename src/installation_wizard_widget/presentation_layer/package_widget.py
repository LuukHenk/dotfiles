from typing import Final

from PySide6.QtCore import Signal, Qt, Slot
from PySide6.QtWidgets import QCheckBox

from data_models.package import Package


class PackageWidget(QCheckBox):
    __PACKAGE_TEXT_TEMPLATE: Final[str] = "{install_text}  {package_name} version {version} ({other})"
    __INSTALL_TEXT: Final[str] = "Install"
    __UNINSTALL_TEXT: Final[str] = "Uninstall"
    updatePackageState = Signal(int, int)  # Tuple[package ID, package state]

    def __init__(self, package: Package, parent=None):
        self.__id = package.id_
        package_text = self.__PACKAGE_TEXT_TEMPLATE.format(
            install_text=self.__UNINSTALL_TEXT if package.installed else self.__INSTALL_TEXT,
            package_name=package.name,
            version=package.version.name,
            other=f"{package.manager_name.value.title()} - {package.version.type.value}",
        )
        super().__init__(package_text, parent=parent)
        self.updatePackageState.connect(self.__on_package_state_changed)

    @Slot(int, int)
    def __on_package_state_changed(self, package_id: int, package_state: int):
        if package_id != self.__id:
            return
        self.blockSignals(True)
        self.setCheckState(Qt.CheckState(package_state))
        self.blockSignals(False)
