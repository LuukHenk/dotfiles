from PySide6.QtCore import Qt, QEvent, QObject
from PySide6.QtWidgets import QWidget, QHBoxLayout, QSpacerItem, QSizePolicy, QCheckBox

from installation_wizard.presentation_layer.designed_package_widget.label import Label
from installation_wizard.presentation_layer.designed_package_widget.stylesheet import (
    get_default_checkbox_stylesheet,
    get_checkbox_stylesheet_on_hover,
    PACKAGE_WIDGET_STYLESHEET,
)


class PackageWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet(PACKAGE_WIDGET_STYLESHEET)
        self.__checkbox = QCheckBox()
        self.__label = Label()
        self.__create_layout()
        self.__set_default_stylesheets()
        self.installEventFilter(self)

    def __create_layout(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        layout.addWidget(self.__checkbox, alignment=Qt.AlignLeft)
        layout.addWidget(self.__label, alignment=Qt.AlignLeft)
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Fixed))

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Enter:
            self.__set_stylesheets_on_hover()
        elif event.type() == QEvent.Leave:
            self.__set_default_stylesheets()
        return False

    def __set_stylesheets_on_hover(self):
        self.__checkbox.setStyleSheet(get_checkbox_stylesheet_on_hover())
        self.__label.set_stylesheets_on_hover()

    def __set_default_stylesheets(self):
        self.__checkbox.setStyleSheet(get_default_checkbox_stylesheet())
        self.__label.set_default_stylesheets()
