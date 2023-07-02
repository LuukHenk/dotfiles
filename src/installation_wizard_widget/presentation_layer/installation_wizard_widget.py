from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QGridLayout, QWidget, QPushButton

from installation_wizard_widget.presentation_layer.groups_panel import GroupsPanel
from installation_wizard_widget.presentation_layer.packages_group_panel import PackagesGroupPanel


class InstallationWizardWidget(QWidget):
    install = Signal()

    def __init__(
        self,
        groups_panel: GroupsPanel,
        active_packages_group_panel: PackagesGroupPanel,
        parent=None,
    ):
        super().__init__(parent)
        self.__active_packages_group_panel = active_packages_group_panel
        self.__apply_button = self.__create_apply_button()
        self.__create_layout(groups_panel)

    def __create_layout(self, groups_panel: GroupsPanel):
        layout = QGridLayout(self)
        layout.addWidget(groups_panel, 0, 0, Qt.AlignTop)
        layout.addWidget(self.__active_packages_group_panel, 0, 1, Qt.AlignTop)
        layout.addWidget(self.__apply_button, 1, 0, 1, 0, Qt.AlignBottom)

    def __create_apply_button(self) -> QPushButton:
        apply_button = QPushButton("Apply changes")
        apply_button.clicked.connect(self.install)
        apply_button.setDisabled(True)
        return apply_button
