from sys import argv, exit as sys_exit
from PySide6.QtWidgets import QApplication

from configuration_loader.configuration_loader import ConfigurationLoader
from data_layer.package_accessor import PackageAccessor
from installation_wizard.installation_wizard import InstallationWizard
from installer.installer import Installer


def run_application():
    app = QApplication(argv)
    package_accessor = PackageAccessor()
    ConfigurationLoader().load_packages(package_accessor)
    installer = Installer(package_accessor)
    installation_wizard = InstallationWizard(package_accessor, installer.install)
    installation_wizard.show()
    sys_exit(app.exec_())
