import time

from PySide6.QtCore import QObject, Signal
from data_models.package_info import PackageInfo
from data_layer.package_accessor import PackageAccessor


class PackageInstaller(QObject):

    installationPercentageUpdated = Signal(int)
    newInstallationLogMessage = Signal(str)

    def __init__(self, package_accessor: PackageAccessor, parent=None):
        super().__init__(parent=parent)
        self.__package_accessor = package_accessor

    def install_packages(self):
        packages = self.__package_accessor.find_packages_with_an_installation_request()
        self.installationPercentageUpdated.emit(0)
        for i, package in enumerate(packages):
            percentage_done = int(i / len(packages) * 100)
            self.installationPercentageUpdated.emit(percentage_done)
        self.installationPercentageUpdated.emit(100)

    def __install_package(self, package: PackageInfo):
        pass

    def __uninstall_package(self, package: PackageInfo):
        pass
