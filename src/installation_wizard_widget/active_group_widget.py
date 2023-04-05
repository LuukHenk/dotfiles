from sys import exit as sys_exit, argv

from typing import Dict, Final, List
from PySide6.QtWidgets import (
    QWidget,
    QApplication,
    QVBoxLayout,
    QLabel,
    QCheckBox,
    QStackedWidget,
)
from data_models.manager import Manager

from data_models.package_info import PackageInfo
from data_models.version import Version


class ActiveGroupWidget(QStackedWidget):

    PACKAGE_TEXT_TEMPLATE: Final[str] = "{install_text}  v{version} ({other})"
    INSTALL_TEXT: Final[str] = "Install"
    UNINSTALL_TEXT: Final[str] = "Uninstall"

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.__groups: Dict[str, QWidget] = {}

    def add_group(self, group_name: str, packages: List[PackageInfo]) -> None:
        group = QWidget()
        group_layout = QVBoxLayout(group)
        group_layout.addWidget(QLabel(group_name))
        for package in packages:
            group_layout.addWidget(self.__create_package_checkbox(package))
        self.__groups[group_name] = group
        self.addWidget(group)

    def update_active_group(self, group_name: str):
        self.setCurrentWidget(self.__groups[group_name])

    def __create_package_checkbox(self, package_info: PackageInfo) -> QCheckBox:
        package_text = self.PACKAGE_TEXT_TEMPLATE.format(
            install_text=self.UNINSTALL_TEXT if package_info.installed else self.INSTALL_TEXT,
            package_name=package_info.name,
            version=package_info.version[0],
            other=f"{package_info.manager.title()} - {package_info.version[1].value}",
        )
        return QCheckBox(package_text)


if __name__ == "__main__":

    packages_ = [
        PackageInfo(
            name="python3",
            version=("3.10.6-1~22.04", Version.LATEST_STABLE),
            installed=True,
            manager=Manager.APT,
        ),
        PackageInfo(
            name="python2",
            version=("2.7.18-3", Version.LATEST_STABLE),
            installed=False,
            manager=Manager.APT,
        ),
    ]
    app = QApplication(argv)
    window = ActiveGroupWidget()
    window.update_active_group("Python")
    window.show()
    sys_exit(app.exec())
