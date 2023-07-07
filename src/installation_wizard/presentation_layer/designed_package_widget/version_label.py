from PySide6.QtWidgets import QLabel

from installation_wizard.presentation_layer.designed_package_widget.style import VERSION_LABEL_NAME


class VersionLabel(QLabel):
    def __init__(self, text: str, parent=None):
        super().__init__(text=text, parent=parent)
        self.setObjectName(VERSION_LABEL_NAME)
