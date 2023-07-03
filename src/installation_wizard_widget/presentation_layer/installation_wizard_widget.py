from typing import List

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QGridLayout, QWidget, QPushButton

from installation_wizard_widget.business_layer.packages_group_panel_handler import PackagesGroupPanelHandler
from installation_wizard_widget.presentation_layer.groups_panel import GroupsPanel
from installation_wizard_widget.presentation_layer.packages_group_panel import PackagesGroupPanel


class InstallationWizardWidget(QWidget):
    install = Signal()

    def __init__(
        self,
        group_names: List[str],
        packages_group_panel_handler: PackagesGroupPanelHandler,
        parent=None,
    ):
        super().__init__(parent)
        self.__packages_group_panel_handler = packages_group_panel_handler
        self.__active_packages_group_panel = self.__packages_group_panel_handler.get_groups_panel(group_names[0])
        self.__groups_panel = GroupsPanel(group_names)
        self.__apply_button = self.__create_apply_button()
        self.__layout = self.__create_layout()
        self.__groups_panel.groupClicked.connect(self.__on_group_clicked)

    def __create_layout(self) -> QGridLayout:
        layout = QGridLayout(self)
        layout.addWidget(self.__groups_panel, 0, 0, Qt.AlignTop)
        layout.addWidget(self.__active_packages_group_panel, 0, 1, Qt.AlignTop)
        layout.addWidget(self.__apply_button, 1, 0, 1, 0, Qt.AlignBottom)
        return layout

    def __create_apply_button(self) -> QPushButton:
        apply_button = QPushButton("Apply changes")
        apply_button.clicked.connect(self.install)
        apply_button.clicked.connect(self.__on_apply)
        apply_button.setDisabled(False)
        return apply_button

    @Slot(str)
    def __on_group_clicked(self, group_name: str):
        new_active_widget = self.__packages_group_panel_handler.get_groups_panel(group_name)
        self.__layout.replaceWidget(self.__active_packages_group_panel, new_active_widget)
        self.__active_packages_group_panel = new_active_widget

    @Slot()
    def __on_apply(self):
        print("applying")
