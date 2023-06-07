import time

from PySide6.QtWidgets import QWidget, QGridLayout, QMessageBox
from PySide6.QtCore import Qt, Signal

from data_layer.package_accessor import PackageAccessor
from installation_wizard_widget.active_group_widget import ActiveGroupWidget
from installation_wizard_widget.group_panel_widget import GroupPanelWidget
from installation_wizard_widget.controls_widget import ControlsWidget
from installation_wizard_widget.confirmation_widget import ConfirmationWidget


class InstallationWizardWidget(QWidget):
    install = Signal()

    def __init__(self, package_accessor: PackageAccessor, parent=None) -> None:
        super().__init__(parent)
        self.__package_accessor = package_accessor

        self.__active_group_widget = self.__construct_active_group_widget()
        self.__active_group_widget.InstallationRequest.connect(
            self.__package_accessor.update_installation_request_status)

        self.__groups_widget = GroupPanelWidget(list(self.__package_accessor.package_info_groups))
        self.__groups_widget.groupClicked.connect(self.__on_active_group_changed)

        self.__controls_widget = ControlsWidget()
        self.__controls_widget.InstallClicked.connect(self.__show_confirmation_widget)

        self.__create_layout()

    def __create_layout(self) -> None:
        layout = QGridLayout(self)
        layout.addWidget(self.__groups_widget, 0, 0, Qt.AlignTop)
        layout.addWidget(self.__active_group_widget, 0, 1, Qt.AlignTop)
        layout.addWidget(self.__controls_widget, 1, 0, 1, 0, Qt.AlignBottom)

    def __construct_active_group_widget(self) -> ActiveGroupWidget:
        active_group_widget = ActiveGroupWidget()
        for group_name, packages in self.__package_accessor.package_info_groups.items():
            active_group_widget.add_group(
                group_name=group_name,
                packages=packages
            )
        return active_group_widget

    def __on_active_group_changed(self, new_group: str) -> None:
        self.__active_group_widget.update_active_group(new_group)

    def __show_confirmation_widget(self):
        packages_to_install = self.__package_accessor.find_packages_with_an_installation_request()
        confirmation_widget = ConfirmationWidget(packages_to_install)
        install_packages = confirmation_widget.exec()
        if install_packages == QMessageBox.Yes:
            self.setDisabled(True)
            self.install_event()

    def install_event(self):
        self.install.emit()
        self.close()
