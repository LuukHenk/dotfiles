from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QHBoxLayout

from data_models.package import Package
from installation_wizard.presentation_layer.package_checkbox.manager_label import ManagerLabel
from stylesheet.data_layer.object_names import PACKAGE_LABEL
from installation_wizard.presentation_layer.package_checkbox.version_label import VersionLabel


class PackageLabel(QPushButton):
    def __init__(self, package: Package, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(PACKAGE_LABEL)
        install_text = "Uninstall" if package.installed else "Install"
        self.__version_label = VersionLabel(f"{install_text} {package.version.name}")
        self.__manager_label = ManagerLabel(package.manager_name)
        self.__create_layout()
        self.setFixedWidth(200)

    def __create_layout(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 0, 0)
        layout.addWidget(self.__version_label)
        layout.addWidget(self.__manager_label, alignment=Qt.AlignRight)
