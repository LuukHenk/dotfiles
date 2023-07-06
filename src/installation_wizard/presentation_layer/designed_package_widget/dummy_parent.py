from PySide6.QtWidgets import QWidget, QHBoxLayout

from installation_wizard.presentation_layer.designed_package_widget.package_widget import PackageWidget


class DummyParent(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        layout = QHBoxLayout(self)
        package = PackageWidget()
        layout.addWidget(package)
