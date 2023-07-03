from typing import List

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QGridLayout, QWidget, QPushButton

from installation_wizard_widget.business_layer.id_tracker import IdTracker
from installation_wizard_widget.presentation_layer.groups_panel import GroupsPanel
from installation_wizard_widget.presentation_layer.stacked_group_panels import StackedGroupPanels


class InstallationWizardWidget(QWidget):
    install = Signal()

    def __init__(
        self,
        group_names: List[str],
        stacked_group_panels: StackedGroupPanels,
        package_id_tracker: IdTracker,
        parent=None,
    ):
        super().__init__(parent)
        self.__stacked_group_panels = stacked_group_panels
        self.__groups_panel = GroupsPanel(group_names)
        self.__apply_button = self.__create_apply_button()
        self.__package_id_tracker = package_id_tracker

        self.__layout = self.__create_layout()
        self.__groups_panel.groupClicked.connect(self.__on_group_clicked)
        self.__stacked_group_panels.packageStateChange.connect(self.__update_packages_to_install)
        if len(group_names):
            self.__groups_panel.check_group(group_names[0])

    def __create_layout(self) -> QGridLayout:
        layout = QGridLayout(self)
        layout.addWidget(self.__groups_panel, 0, 0, Qt.AlignTop)
        layout.addWidget(self.__stacked_group_panels, 0, 1, Qt.AlignTop)
        layout.addWidget(self.__apply_button, 1, 0, 1, 0, Qt.AlignBottom)
        return layout

    def __create_apply_button(self) -> QPushButton:
        apply_button = QPushButton("Apply changes")
        apply_button.clicked.connect(self.install)
        apply_button.setDisabled(True)
        return apply_button

    @Slot(str)
    def __on_group_clicked(self, group_name: str):
        self.__stacked_group_panels.switch_group_panel(group_name)

    @Slot(int, int)
    def __update_packages_to_install(self, package_id: int, state: int):
        if state == Qt.Checked.value:
            self.__package_id_tracker.add_id(package_id)
        if state == Qt.Unchecked.value:
            self.__package_id_tracker.remove_id(package_id)
        self.__apply_button.setEnabled(len(self.__package_id_tracker.ids))
