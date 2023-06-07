

from typing import List
from PySide6.QtWidgets import QMessageBox
from data_models.package_info import PackageInfo
from installation_wizard_widget.package_info_text_generator import generate_package_info_text



class ConfirmationWidget(QMessageBox):
    def __init__(self, packages: List[PackageInfo]):
        super().__init__()
        self.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        self.setWindowTitle("Update packages?")
        text = "\n".join([f"- {generate_package_info_text(package)} ?" for package in packages])
        self.setText(text)


