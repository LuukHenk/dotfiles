from typing import List, Dict

from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QGridLayout, QWidget, QFrame

from data_models.package_old import PackageOld
from installation_wizard.business_layer.installation_wizard_processor import InstallationWizardProcessor
from installation_wizard.data_layer.typing_hints import NestedPackageGroups
from installation_wizard.presentation_layer.apply_button import ApplyButton
from installation_wizard.presentation_layer.confirmation_widget import ConfirmationWidget
from installation_wizard.presentation_layer.groups_panel import GroupsPanel
from installation_wizard.presentation_layer.stacked_packages_panels import StackedPackagesPanels
from stylesheet.data_layer.defaults import BORDER_SIZE_INT
from stylesheet.data_layer.object_names import GROUPS_PANEL_LINE


class InstallationWizardWidget(QWidget):
    install = Signal()

    __INSTALLATION_APPROVED_ID = 16384

    def __init__(
        self,
        group_data: NestedPackageGroups,
        installation_wizard_processor: InstallationWizardProcessor,
        parent=None,
    ):
        super().__init__(parent)
        group_names = sorted(group_data.keys())
        self.__stacked_group_panels = self.__construct_stacked_group_panels(group_data)
        self.__groups_panel = GroupsPanel(group_names)
        self.__apply_button = ApplyButton()
        self.__installation_wizard_processor = installation_wizard_processor

        self.__layout = self.__create_layout()

        self.__apply_button.clicked.connect(self.__show_confirmation_widget)
        self.__groups_panel.groupClicked.connect(self.__on_group_clicked)
        self.__stacked_group_panels.packageChecked.connect(self.__update_packages_to_install)

        if len(group_names):
            self.__groups_panel.check_group(group_names[0])

    def __create_layout(self) -> QGridLayout:
        layout = QGridLayout(self)
        layout.setSpacing(0)
        layout.addWidget(self.__groups_panel, 0, 0, Qt.AlignTop)
        layout.addWidget(self.__create_line(), 0, 1, 2, 1)
        layout.addWidget(self.__stacked_group_panels, 0, 2, Qt.AlignTop)
        layout.addWidget(self.__apply_button, 1, 2, Qt.AlignBottom | Qt.AlignRight)
        return layout

    def __show_confirmation_widget(self):
        packages_to_install = self.__installation_wizard_processor.get_packages_to_install()
        confirmation_widget = ConfirmationWidget(packages_to_install)
        install_packages = confirmation_widget.exec()
        if install_packages == self.__INSTALLATION_APPROVED_ID:
            self.setDisabled(True)
            self.__installation_wizard_processor.set_installation_requests()
            self.install.emit()

    @staticmethod
    def __create_line() -> QFrame:
        line = QFrame()
        line.setObjectName(GROUPS_PANEL_LINE)
        line.setFrameShape(QFrame.VLine)
        line.setLineWidth(BORDER_SIZE_INT)
        return line

    @staticmethod
    def __construct_stacked_group_panels(group_data: NestedPackageGroups) -> StackedPackagesPanels:
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
