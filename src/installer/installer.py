from time import sleep

from data_layer.package_accessor import PackageAccessor
from data_models.package_old import PackageOld

from installer.installing_status_widget.installation_status_widget import InstallationStatusWidget
from package_manager_manager.package_manager_manager import PackageManagerManager


class Installer:
    def __init__(self, package_accessor: PackageAccessor) -> None:
        self.__package_accessor = package_accessor
        self.__installation_status_widget = InstallationStatusWidget()
        self.__package_manager_manager = PackageManagerManager()

    @property
    def installation_status_widget(self):
        return self.__installation_status_widget

    def install(self):
        packages_to_install = self.__package_accessor.find(installation_request=True)
        for i, package in enumerate(packages_to_install):
            self.__install_package(package)
            percentage_done = int((i + 1) / len(packages_to_install) * 100)
            self.__installation_status_widget.update_progress_bar(percentage_done)

    def __install_package(self, package: PackageOld):
        install_status = "Uninstalling" if package.installed else "Installing"
        self.__installation_status_widget.add_message(f"{install_status} {package.name} {package.version.name}...")
        result = self.__package_manager_manager.swap_installation_status(package)
        if result.success:
            package.installed = not package.installed
            package.installation_request = False
            self.__package_accessor.update_package(package.id_, package)
        self.__installation_status_widget.add_message(result.message)
