from typing import List
from PySide6.QtWidgets import QMessageBox

from data_models.package import Package
from installation_wizard_widget.business_layer.package_info_text_generator import generate_package_text


class ConfirmationWidget(QMessageBox):
    def __init__(self, packages: List[Package]):
        super().__init__()
        self.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        self.setWindowTitle("Update packages?")
        text = "\n".join([f"- {generate_package_text(package)} ?" for package in packages])
        self.setText(text)
