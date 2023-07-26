from sys import argv, exit as sys_exit
from typing import List

from PySide6.QtCore import Qt, QObject, Slot
from PySide6.QtWidgets import QApplication

from configuration_loader.configuration_loader import ConfigurationLoader
from data_models.item import Item
from installation_wizard.installation_wizard import InstallationWizard
from installer.installer import Installer
from application.main_window import MainWindow


def run_application():
    qt_app = QApplication(argv)
    main_app = MainApplication()
    main_app.show_main_window()
    sys_exit(qt_app.exec_())


class MainApplication(QObject):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        config = ConfigurationLoader().load_config()
        self.__installation_wizard = InstallationWizard(config)
        self.__installer = Installer()
        self.__main_window = MainWindow(
            self.__installation_wizard.installation_wizard_widget,
            self.__installer.installation_status_widget,
        )
        self.__installation_wizard.install.connect(self.__on_installation_request, type=Qt.QueuedConnection)
        self.__main_window.readyForInstallation.connect(self.__start_installation, type=Qt.QueuedConnection)

    def show_main_window(self):
        self.__main_window.show()

    @Slot(object)
    def __on_installation_request(self, items_to_install: List[Item]):
        self.__installer.set_items_to_install(items_to_install)
        self.__main_window.show_installation_status_widget()

    def __start_installation(self):
        self.__installer.install()
