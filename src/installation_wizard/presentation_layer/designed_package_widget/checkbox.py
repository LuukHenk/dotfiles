from PySide6.QtWidgets import QCheckBox

from installation_wizard.presentation_layer.designed_package_widget.stylesheet import CHECKBOX_STYLESHEET


class CheckBox(QCheckBox):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet(CHECKBOX_STYLESHEET)
