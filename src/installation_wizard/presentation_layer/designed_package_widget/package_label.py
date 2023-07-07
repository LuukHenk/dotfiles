from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QHBoxLayout

from data_models.package import Package
from installation_wizard.presentation_layer.designed_package_widget.manager_label import ManagerLabel
from installation_wizard.presentation_layer.style import PACKAGE_LABEL_NAME
from installation_wizard.presentation_layer.designed_package_widget.version_label import VersionLabel


class PackageLabel(QPushButton):
    def __init__(self, package: Package, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(PACKAGE_LABEL_NAME)
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
