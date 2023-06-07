

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
        self.__group_widget = GroupPanelWidget(list(self.__processor.package_info_groups))
        self.__group_widget.groupClicked.connect(self.__on_active_group_changed)

        self.__create_layout()

    def __create_layout(self) -> None:
        layout = QGridLayout(self)
        layout.addWidget(self.__group_widget, 0, 0, Qt.AlignLeft) #type:ignore
        layout.addWidget(self.__active_group_widget, 0, 1, Qt.AlignCenter) #type:ignore

    def __construct_active_group_widget(self) -> ActiveGroupWidget:
        active_group_widget = ActiveGroupWidget()
        for group_name, packages in self.__processor.package_info_groups.items():
            active_group_widget.add_group(
                group_name=group_name,
                packages=packages
            )
        return active_group_widget
    
    def __on_active_group_changed(self, new_group: str) -> None:
        self.__active_group_widget.update_active_group(new_group)