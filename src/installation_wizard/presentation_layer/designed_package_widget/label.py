from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QHBoxLayout

from data_models.manager_name import ManagerName
from installation_wizard.presentation_layer.designed_package_widget.manager_label import ManagerLabel
from installation_wizard.presentation_layer.designed_package_widget.version_label import VersionLabel


class Label(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__version_label = VersionLabel("V1.00005")
        self.__manager_label = ManagerLabel(ManagerName.APT)
        self.__create_layout()
        self.setFixedWidth(200)

    def __create_layout(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(10, 0, 0, 0)
        layout.addWidget(self.__version_label)
        layout.addWidget(self.__manager_label, alignment=Qt.AlignRight)
