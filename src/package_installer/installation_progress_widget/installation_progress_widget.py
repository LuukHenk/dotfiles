
from PySide6.QtWidgets import QWidget, QVBoxLayout, QProgressBar, QTextEdit

from package_installer.package_installer import PackageInstaller


class InstallationProgressWidget(QWidget):

    def __init__(self, package_installer: PackageInstaller, parent=None):
        super().__init__(parent)
        self.__progress_bar = QProgressBar()
        self.__log = QTextEdit()
        self.__log.setReadOnly(True)
        self.__package_installer = self.__setup_package_installer(package_installer)
        self.__create_layout()

    def show(self) -> None:
        super().show()
        self.__package_installer.install_packages()

    def __setup_package_installer(self, package_installer) -> PackageInstaller:
        package_installer.installationPercentageUpdated.connect(self.__progress_bar.setValue)
        package_installer.newInstallationLogMessage.connect(self.__log.append)
        return package_installer

    def __create_layout(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.__progress_bar)
        layout.addWidget(self.__log)
