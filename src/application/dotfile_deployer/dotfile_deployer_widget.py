from typing import List

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QCheckBox, QMessageBox
from PySide6.QtCore import Qt

from src.application.dotfile_deployer.dotfile import Dotfile

class DotfileDeployerWidget(QWidget):
    def __init__(self, dotfiles: List[Dotfile]) -> None:
        super().__init__()
        self.__checkboxes: List[QCheckBox] = []
        dotfile_deployer_layout = QVBoxLayout()
        dotfile_deployer_layout.addWidget(QLabel("<b>Deploy dotfiles<\\b>"))
        dotfile_deployer_layout.addWidget(self.__create_checkbox_widget(dotfiles))
        self.setLayout(dotfile_deployer_layout)

    def get_checked_dotfiles(self) -> List[str]:
        checked_packages = []
        for checkbox in self.__checkboxes:
            if checkbox.checkState() == Qt.Checked:
                checked_packages.append(checkbox.text())
        return checked_packages

    def overwrite_dialog(self, message: str) -> bool:
        dialog = QMessageBox(text=message)
        dialog.setStandardButtons(QMessageBox.Cancel| QMessageBox.Ok)
        return dialog.exec() == QMessageBox.Ok
        

    def __create_checkbox_widget(self, dotfiles: List[Dotfile]) -> QWidget:
        checkboxes_widget = QWidget()
        checkbox_layout = QVBoxLayout()
        for dotfile in dotfiles:
            dotfile_checkbox = QCheckBox(dotfile.name)
            dotfile_checkbox.setChecked(False)
            self.__checkboxes.append(dotfile_checkbox)
            checkbox_layout.addWidget(dotfile_checkbox)
        checkboxes_widget.setLayout(checkbox_layout)
        return checkboxes_widget