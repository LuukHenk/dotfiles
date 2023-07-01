from PySide6.QtCore import QObject, Signal
from typing import Dict

from old.data_models import Manager
from old.data_models.package_info import PackageInfo
from old.data_layer.package_accessor import PackageAccessor
from old.package_installer.package_managers.apt_package_installer import AptPackageInstaller
from old.package_installer.package_managers.package_installer import PackageInstaller
from old.utils.logger.logger import log_error, log_info


class PackagesInstaller(QObject):
    installationPercentageUpdated = Signal(int)
    newInstallationLogMessage = Signal(str)

    def __init__(self, package_accessor: PackageAccessor, parent=None):
        super().__init__(parent=parent)
        self.__package_accessor = package_accessor
        self.__package_managers: Dict[Manager, PackageInstaller] = {Manager.APT: AptPackageInstaller()}

    def install_packages(self):
        packages = self.__package_accessor.find_packages_with_an_installation_request()
        self.installationPercentageUpdated.emit(0)
        for i, package in enumerate(packages):
            self.__install_package(package)
            percentage_done = int(i / len(packages) * 100)
            self.installationPercentageUpdated.emit(percentage_done)
        self.installationPercentageUpdated.emit(100)

    def __install_package(self, package: PackageInfo) -> None:
        if package.manager not in self.__package_managers:
            self.__publish_fail_message(
                package.name,
                f"Package manager {package.manager} for package {package.name} not found in the installer.",
            )
            return
        success, error_message = self.__package_managers[package.manager].swap_installation_status(package)
        if not success:
            self.__publish_fail_message(package.name, error_message)
            return
        success_message = f"Successfully installed {package.name}"
        log_info(success_message)
        self.newInstallationLogMessage.emit(success_message)

    def __publish_fail_message(self, package_name: str, message: str) -> None:
        message = f"Failed to install {package_name}. {message}"
        log_error(message)
        self.newInstallationLogMessage.emit(message)
