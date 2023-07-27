from typing import List
from PySide6.QtWidgets import QMessageBox

from data_models.item import Item
from data_models.package import Package
from installation_wizard.business_layer.widget_text_generator import generate_text


class ConfirmationWidget(QMessageBox):
    def __init__(self, items: List[Item], parent=None):
        super().__init__(parent)
        self.setStandardButtons(QMessageBox.No | QMessageBox.Yes)
        self.setWindowTitle("Update items?")
        text = "\n".join([f"- {generate_text(item)} ?" for item in items])
        self.setText(text)
