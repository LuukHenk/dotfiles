from PySide6.QtWidgets import QLabel
from stylesheet.sub_stylesheets.package_stylesheet import DEFAULT_HEIGHT
from stylesheet.data_layer.object_names import PACKAGE_VERSION


class VersionLabel(QLabel):
    def __init__(self, text: str, parent=None):
        super().__init__(text=text, parent=parent)
        self.setObjectName(PACKAGE_VERSION)
        self.setFixedHeight(DEFAULT_HEIGHT - 2)
