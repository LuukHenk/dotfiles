from PySide6.QtWidgets import QWidget, QGridLayout, QMessageBox
from PySide6.QtCore import Qt, Signal

from old.data_layer.package_accessor import PackageAccessor
from old.data_models.package_info import PackageInfo
from old.installation_wizard_widget.active_group_widget import ActiveGroupWidget
from old.installation_wizard_widget.group_selection_widget import GroupSelectionWidget
from old.installation_wizard_widget.controls_widget import ControlsWidget
from old.installation_wizard_widget.confirmation_widget import ConfirmationWidget


class InstallationWizardWidget(QWidget):
    install = Signal()

    def __init__(self, package_accessor: PackageAccessor, parent=None) -> None:
        super().__init__(parent)
        self.__package_accessor = package_accessor

        self.__active_group_widget = self.__construct_active_group_widget()
        self.__active_group_widget.InstallationRequestUpdate.connect(self.__on_installation_request_update)

        # self.__group_widgets: Dict[str, GroupWidget] = self.__construct_group_widgets()
        self.__group_selection_widget = GroupSelectionWidget(self.__package_accessor.get_package_group_names())
        self.__group_selection_widget.groupClicked.connect(self.__on_active_group_changed)

        self.__controls_widget = ControlsWidget()
        self.__controls_widget.InstallClicked.connect(self.__show_confirmation_widget)

        self.__create_layout()

    def __create_layout(self) -> None:
        layout = QGridLayout(self)
        layout.addWidget(self.__group_selection_widget, 0, 0, Qt.AlignTop)
        layout.addWidget(self.__active_group_widget, 0, 1, Qt.AlignTop)
        layout.addWidget(self.__controls_widget, 1, 0, 1, 0, Qt.AlignBottom)

    def __construct_active_group_widget(self) -> ActiveGroupWidget:
        active_group_widget = ActiveGroupWidget()
        groups = self.__package_accessor.get_package_group_names()
        for group in groups:
            active_group_widget.add_group(
                group_name=group, packages=self.__package_accessor.get_packages_in_group(group)
            )
        return active_group_widget

    # def __construct_group_widgets(self) -> Dict[str, GroupWidget]:
    #     group_names = self.__package_accessor.get_package_group_names()
    #     for group_name in group_names:
    #         group_widget = GroupWidget()
    #         packages = self.__package_accessor.get_packages_in_group(group_name)
    #         for package in packages:
    #             group_widget.add_package()

    def __on_active_group_changed(self, new_group: str) -> None:
        self.__active_group_widget.update_active_group(new_group)

    def __on_installation_request_update(self, package: PackageInfo) -> None:
        self.__package_accessor.update_installation_request_status(package)
        self.__controls_widget.setEnabled(self.__package_accessor.any_installation_request())
        self.__group_selection_widget.highlight_groups(
            self.__package_accessor.find_package_groups_with_an_installation_request()
        )

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
