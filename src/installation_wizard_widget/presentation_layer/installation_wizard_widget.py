from typing import List

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QGridLayout, QWidget, QPushButton, QMessageBox

from installation_wizard_widget.business_layer.id_tracker import IdTracker
from installation_wizard_widget.business_layer.installation_wizard_processor import InstallationWizardProcessor
from installation_wizard_widget.presentation_layer.confirmation_widget import ConfirmationWidget
from installation_wizard_widget.presentation_layer.groups_panel import GroupsPanel
from installation_wizard_widget.presentation_layer.stacked_group_panels import StackedGroupPanels


class InstallationWizardWidget(QWidget):
    install = Signal()

    def __init__(
        self,
        group_names: List[str],
        stacked_group_panels: StackedGroupPanels,
        installation_wizard_processor: InstallationWizardProcessor,
        parent=None,
    ):
        super().__init__(parent)
        self.__stacked_group_panels = stacked_group_panels
        self.__groups_panel = GroupsPanel(group_names)
        self.__apply_button = self.__create_apply_button()
        self.__installation_wizard_processor = installation_wizard_processor

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
        apply_button.clicked.connect(self.__show_confirmation_widget)
        apply_button.setDisabled(True)
        return apply_button

    def __show_confirmation_widget(self):
        packages_to_install = self.__installation_wizard_processor.get_packages_to_install()
        confirmation_widget = ConfirmationWidget(packages_to_install)
        install_packages = confirmation_widget.exec()
        if install_packages == QMessageBox.Yes:
            self.setDisabled(True)
            self.__installation_wizard_processor.set_installation_requests()
            self.install_event()

    @Slot(str)
    def __on_group_clicked(self, group_name: str):
        self.__stacked_group_panels.switch_group_panel(group_name)

    @Slot(int, int)
    def __update_packages_to_install(self, package_id: int, state: int):
        state_as_bool = state == Qt.Checked.value
        self.__installation_wizard_processor.update_packages_to_install(package_id, state_as_bool)
        self.__apply_button.setEnabled(self.__installation_wizard_processor.any_selected_packages())

    @Slot()
    def install_event(self):
        self.install.emit()
        self.close()
