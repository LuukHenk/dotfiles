from sys import exit as sys_exit, argv

from typing import Dict, List
from PySide6.QtWidgets import (
    QWidget,
    QApplication,
    QVBoxLayout,
    QLabel,
    QCheckBox,
    QStackedWidget,
)
from PySide6.QtCore import Signal

from data_models.manager import Manager
from data_models.package_info import PackageInfo
from data_models.version import Version
from installation_wizard_widget.package_info_text_generator import generate_package_info_text

class ActiveGroupWidget(QStackedWidget):

    InstallationRequest = Signal(PackageInfo)

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

    def update_active_group(self, group_name: str) -> None:
        self.setCurrentWidget(self.__groups[group_name])

    def __create_package_checkbox(self, package_info: PackageInfo) -> QCheckBox:
        checkbox = QCheckBox(generate_package_info_text(package_info))
        checkbox.clicked.connect(lambda: self.__on_package_checkbox_clicked(package_info))
        return checkbox

    def __on_package_checkbox_clicked(self, package_checkbox_name: PackageInfo) -> None:
        self.InstallationRequest.emit(package_checkbox_name)

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
