
from typing import List
from PySide6.QtWidgets import QWidget, QVBoxLayout, QCheckBox, QLabel
from PySide6.QtCore import Qt
from src.application.package_installer.package import Package

class PackageInstallerWidget(QWidget):

    def __init__(self, packages: List[Package]) -> None:
        super().__init__()
        self.__checkboxes: List[QCheckBox] = []
        package_installer_layout = QVBoxLayout()
        package_installer_layout.addWidget(QLabel("<b>Install packages<\\b>"))
        package_installer_layout.addWidget(self.__create_checkbox_widget(packages))
        self.setLayout(package_installer_layout)

    def get_checked_packages(self) -> List[str]:
        checked_packages = []
        for checkbox in self.__checkboxes:
            if checkbox.checkState() == Qt.Checked:
                checked_packages.append(checkbox.text())
        return checked_packages

    def __create_checkbox_widget(self, packages: List[Package]) -> QWidget:
        checkboxes_widget = QWidget()
        checkbox_layout = QVBoxLayout()
        for package in packages:
            package_checkbox = QCheckBox(package.name)
            package_checkbox.setChecked(False)
            package_checkbox.setDisabled(package.installed)
            self.__checkboxes.append(package_checkbox)
            checkbox_layout.addWidget(package_checkbox)
        checkboxes_widget.setLayout(checkbox_layout)
        return checkboxes_widget