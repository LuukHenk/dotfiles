from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QHBoxLayout

from data_models.package_old import PackageOld
from installation_wizard.presentation_layer.package_checkbox.manager_label import ManagerLabel
from stylesheet.data_layer.object_names import PACKAGE_LABEL
from installation_wizard.presentation_layer.package_checkbox.version_label import VersionLabel


class PackageLabel(QPushButton):
    __MAX_TEXT_LENGTH = 11

    def __init__(self, package: PackageOld, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(PACKAGE_LABEL)
        install_text = "Uninstall" if package.installed else "Install"
        version_text = self.__style_version_text(package.version.name)
        self.__version_label = VersionLabel(f"{install_text} {version_text}")
        self.__manager_label = ManagerLabel(package.manager_name)
        self.__create_layout()
        self.setFixedWidth(200)

    def __create_layout(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 0, 0)
        layout.addWidget(self.__version_label)
        layout.addWidget(self.__manager_label, alignment=Qt.AlignRight)

    def __style_version_text(self, version_text: str) -> str:
        if len(version_text) > self.__MAX_TEXT_LENGTH:
            version_text = version_text[: self.__MAX_TEXT_LENGTH] + "..."
        return version_text
