from PySide6.QtCore import Qt, QObject, QEvent
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QCheckBox, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy

from installation_wizard.presentation_layer.designed_package_widget.package_label import PackageLabel
from installation_wizard.presentation_layer.designed_package_widget.style import (
    PACKAGE_WIDGET_NAME,
    DEFAULT_STYLE,
    HOVER_STYLE,
)


class PackageWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName(PACKAGE_WIDGET_NAME)
        self.__checkbox = QCheckBox()
        self.__package_label = PackageLabel()
        self.__create_layout()
        self.setStyleSheet(DEFAULT_STYLE)
        self.installEventFilter(self)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Enter:
            self.setStyleSheet(HOVER_STYLE)
        elif event.type() == QEvent.Leave:
            self.setStyleSheet(DEFAULT_STYLE)
        return False

    def __create_layout(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        layout.addWidget(self.__checkbox, alignment=Qt.AlignLeft)
        layout.addWidget(self.__package_label, alignment=Qt.AlignLeft)
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Fixed))
