

from PySide6.QtWidgets import QWidget, QGridLayout
from PySide6.QtCore import Qt
from installation_wizard_widget.active_group_widget import ActiveGroupWidget
from installation_wizard_widget.group_panel_widget import GroupPanelWidget
from installation_wizard_widget.installation_wizard_widget_processor import InstallationWizardWidgetProcessor



class InstallationWizardWidget(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.__processor = InstallationWizardWidgetProcessor()
        self.__active_group_widget = self.__construct_active_group_widget()
        self.__group_widget = GroupPanelWidget(self.__processor.get_package_groups())
        self.__group_widget.groupClicked.connect(self.__on_active_group_changed)

        self.__create_layout()

    def __create_layout(self) -> None:
        layout = QGridLayout(self)
        layout.addWidget(self.__group_widget, 0, 0, Qt.AlignLeft) #type:ignore
        layout.addWidget(self.__active_group_widget, 0, 1, Qt.AlignCenter) #type:ignore

    @staticmethod
    def __construct_active_group_widget() -> ActiveGroupWidget:
        active_group_widget = ActiveGroupWidget()
        return active_group_widget
    
    def __on_active_group_changed(self, new_group: str) -> None:
        group_package_info = self.__processor.get_group_package_info(new_group)
        self.__active_group_widget.update_active_group(new_group)