from pathlib import Path
from src.application.application_widget import ApplicationWidget
from src.application.package_installer.package_installer import PackageInstaller

PACKAGES_CONFIG_FILENAME = "packages.json"
class Application:
    def __init__(self):
        self.__repository_path = Path().absolute()/"etc"
        self.__application_widget = ApplicationWidget()
        self.__package_installer = PackageInstaller(
            package_config_file_path=self.__repository_path/PACKAGES_CONFIG_FILENAME
        )
        self.__application_widget.add_widget(self.__package_installer.package_widget)
        

    @property
    def application_widget(self):
        return self.__application_widget