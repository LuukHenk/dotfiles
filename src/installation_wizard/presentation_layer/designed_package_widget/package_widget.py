from PySide6.QtCore import Qt, QObject, QEvent, Slot, Signal
from PySide6.QtWidgets import QCheckBox, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy

from data_models.package import Package
from installation_wizard.presentation_layer.designed_package_widget.package_label import PackageLabel
from installation_wizard.presentation_layer.style import (
    PACKAGE_WIDGET_NAME,
    DEFAULT_STYLE,
    HOVER_STYLE,
)


class PackageWidget(QWidget):
    otherPackageChecked = Signal(int, bool)  # Tuple[package ID, package check state]
    packageChecked = Signal(bool)

    def __init__(self, package: Package, parent=None):
        super().__init__(parent=parent)
        self.__id = package.id_
        self.setObjectName(PACKAGE_WIDGET_NAME)
        self.__checkbox = QCheckBox()
        self.__package_label = PackageLabel(package)
        self.__create_layout()
        self.setStyleSheet(DEFAULT_STYLE)
        self.installEventFilter(self)
        self.__package_label.clicked.connect(self.__swap_package_check_state)
        self.__checkbox.clicked.connect(self.__swap_package_check_state)
        self.otherPackageChecked.connect(self.__on_other_package_checked)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Enter:
            self.setStyleSheet(HOVER_STYLE)
        elif event.type() == QEvent.Leave:
            self.setStyleSheet(DEFAULT_STYLE)
        return False

    @Slot()
    def __swap_package_check_state(self):
        new_check_state = not self.__checkbox.isChecked()
        self.__checkbox.setChecked(new_check_state)
        self.packageChecked.emit(new_check_state)

    def __create_layout(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        layout.addWidget(self.__checkbox, alignment=Qt.AlignLeft)
        layout.addWidget(self.__package_label, alignment=Qt.AlignLeft)
        layout.addSpacerItem(QSpacerItem(0, 0, QSizePolicy.MinimumExpanding, QSizePolicy.Fixed))

    @Slot(int, int)
    def __on_other_package_checked(self, package_id: int, package_state: int):
        if package_id != self.__id:
            return
        self.__checkbox.setChecked(Qt.CheckState(package_state))
