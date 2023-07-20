from PySide6.QtWidgets import QLabel
from stylesheet.data_layer.defaults import BUTTON_HEIGHT_INT
from stylesheet.data_layer.object_names import PACKAGE_VERSION


class VersionLabel(QLabel):
    def __init__(self, text: str, parent=None):
        super().__init__(text=text, parent=parent)
        self.setObjectName(PACKAGE_VERSION)
        self.setFixedHeight(BUTTON_HEIGHT_INT - 2)
