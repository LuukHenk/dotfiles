from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QHBoxLayout, QSpacerItem, QSizePolicy

from installation_wizard.presentation_layer.designed_package_widget.checkbox import CheckBox
from installation_wizard.presentation_layer.designed_package_widget.label import Label
from installation_wizard.presentation_layer.designed_package_widget.stylesheet import PACKAGE_WIDGET_STYLESHEET


class PackageWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet(PACKAGE_WIDGET_STYLESHEET)
        self.__checkbox = CheckBox()
        self.__label = Label()
        self.__create_layout()

    def __create_layout(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        layout.addWidget(self.__checkbox, alignment=Qt.AlignLeft)
        layout.addWidget(self.__label, alignment=Qt.AlignLeft)
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Fixed))
