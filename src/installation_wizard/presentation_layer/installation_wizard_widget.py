from typing import List, Dict

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QGridLayout, QWidget, QPushButton, QMessageBox

from data_models.package import Package
from installation_wizard.business_layer.id_tracker import IdTracker
from installation_wizard.business_layer.installation_wizard_processor import InstallationWizardProcessor
from installation_wizard.presentation_layer.confirmation_widget import ConfirmationWidget
from installation_wizard.presentation_layer.groups_panel import GroupsPanel
from installation_wizard.presentation_layer.stacked_packages_panels import StackedPackagesPanels
from stylesheet.data_layer.object_names import APPLY_BUTTON


class InstallationWizardWidget(QWidget):
    install = Signal()

    __INSTALLATION_APPROVED_ID = 16384

    def __init__(
        self,
        group_data: Dict[str, List[List[Package]]],
        installation_wizard_processor: InstallationWizardProcessor,
        parent=None,
    ):
        super().__init__(parent)
        group_names = list(group_data.keys())
        self.__stacked_group_panels = self.__construct_stacked_group_panels(group_data)
        self.__groups_panel = GroupsPanel(group_names)
        self.__apply_button = self.__create_apply_button()
        self.__installation_wizard_processor = installation_wizard_processor

        self.__layout = self.__create_layout()

        self.__groups_panel.groupClicked.connect(self.__on_group_clicked)
        self.__stacked_group_panels.packageChecked.connect(self.__update_packages_to_install)

        if len(group_names):
            self.__groups_panel.check_group(group_names[0])

    def __create_layout(self) -> QGridLayout:
        layout = QGridLayout(self)
        layout.addWidget(self.__groups_panel, 0, 0, Qt.AlignTop)
        layout.addWidget(self.__stacked_group_panels, 0, 1, Qt.AlignTop)
        layout.addWidget(self.__apply_button, 1, 0, 1, 0, Qt.AlignBottom | Qt.AlignRight)
        return layout

    def __create_apply_button(self) -> QPushButton:
        apply_button = QPushButton("   Apply changes   ")
        apply_button.setObjectName(APPLY_BUTTON)
        apply_button.clicked.connect(self.__show_confirmation_widget)
        apply_button.setDisabled(True)
        return apply_button

    def __show_confirmation_widget(self):
        packages_to_install = self.__installation_wizard_processor.get_packages_to_install()
        confirmation_widget = ConfirmationWidget(packages_to_install)
        install_packages = confirmation_widget.exec()
        if install_packages == self.__INSTALLATION_APPROVED_ID:
            self.setDisabled(True)
            self.__installation_wizard_processor.set_installation_requests()
            self.install.emit()

    @staticmethod
    def __construct_stacked_group_panels(group_data: Dict[str, List[List[Package]]]) -> StackedPackagesPanels:
        stacked_group_panels = StackedPackagesPanels()
        for group_name, package_sets in group_data.items():
            stacked_group_panels.add_group_panel(group_name, package_sets)
        return stacked_group_panels

    @Slot(str)
    def __on_group_clicked(self, group_name: str):
        self.__stacked_group_panels.switch_group_panel(group_name)

    @Slot(int, bool)
    def __update_packages_to_install(self, package_id: int, state: bool):
        self.__installation_wizard_processor.update_packages_to_install(package_id, state)
        self.__apply_button.setEnabled(self.__installation_wizard_processor.any_selected_packages())
