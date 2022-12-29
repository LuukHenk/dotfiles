from pathlib import Path
from PySide6.QtCore import Slot
from src.application.application_widget import ApplicationWidget
from src.application.package_installer.package_installer import PackageInstaller
from src.application.dotfile_deployer.dotfile_deployer import DotfileDeployer

PACKAGES_CONFIG_FILENAME = "packages.json"
DOTFILES_CONFIG_FILENAME = "dotfile_paths.json"
class Application:
    def __init__(self):
        self.__repository_path = Path().absolute()/"etc"
        
        self.__application_widget = ApplicationWidget()
        self.__application_widget.onInstall.connect(self.__on_install)

        self.__package_installer = PackageInstaller(
            package_config_file_path=self.__repository_path/PACKAGES_CONFIG_FILENAME
        )
        self.__application_widget.add_widget(self.__package_installer.package_widget)

        self.__dotfile_deployer = DotfileDeployer(
            dotfiles_config_file_path=self.__repository_path/DOTFILES_CONFIG_FILENAME,
            dotfile_directory=self.__repository_path
        )
        self.__application_widget.add_widget(self.__dotfile_deployer.dotfile_deployer_widget)
        

    @property
    def application_widget(self):
        return self.__application_widget

    @Slot()
    def __on_install(self):
        self.__dotfile_deployer.deploy_dotfiles()
        installation_commands = self.__package_installer.get_installation_commands()
        print(" && ".join(installation_commands))
        
