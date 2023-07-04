import time
from sys import argv, exit as sys_exit
from PySide6.QtWidgets import QApplication

from configuration_loader.configuration_loader import ConfigurationLoader
from data_layer.package_accessor import PackageAccessor
from installation_wizard.installation_wizard import InstallationWizard
from installer.installer import Installer
from application.main_window import MainWindow


def run_application():
    qt_app = QApplication(argv)
    main_app = MainApplication()
    main_app.show_main_window()
    sys_exit(qt_app.exec_())


class MainApplication:
    def __init__(self):
        package_accessor = self.__load_packages()
        self.__installation_wizard = InstallationWizard(package_accessor)
        self.__installer = Installer(package_accessor)
        self.__installation_wizard.set_install_request_callback(self.__on_installation_request)
        self.__main_window = MainWindow(
            self.__installation_wizard.installation_wizard_widget,
            self.__installer.installation_status_widget,
        )

    def show_main_window(self):
        self.__main_window.show()

    def __on_installation_request(self):
        self.__main_window.show_installation_status_widget()
        self.__installer.install()

    @staticmethod
    def __load_packages() -> PackageAccessor:
        package_accessor = PackageAccessor()
        ConfigurationLoader().load_packages(package_accessor)
        return package_accessor
