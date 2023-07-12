from PySide6.QtCore import Qt, QObject, QEvent, Slot, Signal
from PySide6.QtWidgets import QCheckBox, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy

from data_models.package import Package
from installation_wizard.presentation_layer.designed_package_widget.package_label import PackageLabel
from stylesheet.data_layer.object_names import PACKAGE_CHECKBOX, PACKAGE
from stylesheet.stylesheets import StyleSheets


class PackageWidget(QWidget):
    otherPackageChecked = Signal(int, bool)  # Tuple[package ID, package check state]
    packageChecked = Signal(bool)

    def __init__(self, package: Package, parent=None):
        super().__init__(parent=parent)
        self.__id = package.id_
        self.setObjectName(PACKAGE)
        self.__checkbox = QCheckBox()
        self.__checkbox.setObjectName(PACKAGE_CHECKBOX)
        self.__package_label = PackageLabel(package)
        self.__stylesheet_handler = StyleSheets()
        self.__create_layout()
        self.installEventFilter(self)
        self.__package_label.clicked.connect(self.__swap_package_check_state)
        self.__checkbox.clicked.connect(self.__signal_checkbox_state)
        self.otherPackageChecked.connect(self.__on_other_package_checked)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Enter:
            self.setStyleSheet(self.__stylesheet_handler.stylesheet_on_package_hover)
        elif event.type() == QEvent.Leave:
            self.setStyleSheet(self.__stylesheet_handler.default_stylesheet)
        return False

    @Slot()
    def __swap_package_check_state(self):
        new_check_state = not self.__checkbox.isChecked()
        self.__checkbox.setChecked(new_check_state)
        self.__signal_checkbox_state()

    @Slot(bool)
    def __signal_checkbox_state(self):
        self.packageChecked.emit(self.__checkbox.isChecked())
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
