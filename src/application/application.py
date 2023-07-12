from sys import argv, exit as sys_exit

from PySide6.QtCore import Qt, QObject
from PySide6.QtWidgets import QApplication

from configuration_loader.configuration_loader import ConfigurationLoader
from data_layer.package_accessor import PackageAccessor
from installation_wizard.installation_wizard import InstallationWizard
from installation_wizard.presentation_layer.dummy_parent import DummyParent
from installer.installer import Installer
from application.main_window import MainWindow
from stylesheet.stylesheets import StyleSheets

def run_test():
    
    qt_app = QApplication(argv)
    qt_app.setStyleSheet(StyleSheets().default_stylesheet)
    main_app = DummyParent()
    main_app.show()
    sys_exit(qt_app.exec_())


def run_application():
    qt_app = QApplication(argv)
    qt_app.setStyleSheet(StyleSheets().default_stylesheet)
    main_app = MainApplication()
    main_app.show_main_window()
    sys_exit(qt_app.exec_())


class MainApplication(QObject):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        package_accessor = self.__load_packages()
        self.__installation_wizard = InstallationWizard(package_accessor)
        self.__installer = Installer(package_accessor)
        self.__main_window = MainWindow(
            self.__installation_wizard.installation_wizard_widget,
            self.__installer.installation_status_widget,
        )
        self.__installation_wizard.install.connect(self.__on_installation_request, type=Qt.QueuedConnection)
        self.__main_window.readyForInstallation.connect(self.__start_installation, type=Qt.QueuedConnection)

    def show_main_window(self):
        self.__main_window.show()

    def __on_installation_request(self):
        self.__main_window.show_installation_status_widget()

    def __start_installation(self):
        self.__installer.install()

    @staticmethod
    def __load_packages() -> PackageAccessor:
        package_accessor = PackageAccessor()
        ConfigurationLoader().load_packages(package_accessor)
        return package_accessor
