from time import sleep

from data_layer.package_accessor import PackageAccessor

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
        messages = []
        packages_to_install = self.__package_accessor.find(installation_request=True)
        for i, package in enumerate(packages_to_install):
            messages.append(f"Installing {package}...")
            result = self.__package_manager_manager.swap_installation_status(package)
            if result.success:
                package.installed = not package.installed
                package.installation_request = False
                self.__package_accessor.update_package(package.id_, package)
            messages[-1] = result.message
            percentage_done = int(i / len(packages_to_install) * 100)
            self.__installation_status_widget.update_installation_status(percentage_done, messages)
        self.__installation_status_widget.update_installation_status(100, messages)
