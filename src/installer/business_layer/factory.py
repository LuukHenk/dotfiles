from installer.business_layer.installer import Installer
from installer.installing_status_widget.installing_status_widget import InstallationStatusWidget


class Factory:
    def __init__(self):
        self.__installer = self.__create_installer()

    @property
    def installer(self):
        return self.__installer

    @staticmethod
    def __create_installer() -> Installer:
        installation_status_widget = InstallationStatusWidget()
        return Installer(installation_status_widget.update_installation_status)
