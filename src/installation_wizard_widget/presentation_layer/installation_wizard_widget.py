from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QGridLayout, QWidget

from installation_wizard_widget.presentation_layer.apply_button import ApplyButton
from installation_wizard_widget.presentation_layer.groups_panel import GroupsPanel
from installation_wizard_widget.presentation_layer.package_group_panel import PackageGroupPanel


class InstallationWizardWidget(QWidget):
    install = Signal()

    def __init__(self, groups_panel: GroupsPanel, active_package_group_panel: PackageGroupPanel, parent=None):
        super().__init__(parent)
        self.__active_package_group_panel = active_package_group_panel
        self.__create_layout(groups_panel)

    def __create_layout(self, groups_panel: GroupsPanel):
        layout = QGridLayout(self)
        layout.addWidget(groups_panel, 0, 0, Qt.AlignTop)
        layout.addWidget(self.__active_package_group_panel, 0, 1, Qt.AlignTop)
        layout.addWidget(self.__create_apply_button(), 1, 0, 1, 0, Qt.AlignBottom)

    def __create_apply_button(self) -> ApplyButton:
        apply_button = ApplyButton()
        apply_button.clicked.connect(self.install)
        return apply_button
