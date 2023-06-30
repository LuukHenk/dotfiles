
from PySide6.QtWidgets import QWidget, QVBoxLayout, QProgressBar, QTextEdit

from package_installer.packages_installer import PackagesInstaller


class InstallationProgressWidget(QWidget):

    def __init__(self, packages_installer: PackagesInstaller, parent=None):
        super().__init__(parent)
        self.__progress_bar = QProgressBar()
        self.__log = QTextEdit()
        self.__log.setReadOnly(True)
        self.__package_installer = self.__setup_packages_installer(packages_installer)
        self.__create_layout()

    def show(self) -> None:
        super().show()
        self.__package_installer.install_packages()

    def __setup_packages_installer(self, packages_installer) -> PackagesInstaller:
        packages_installer.installationPercentageUpdated.connect(self.__progress_bar.setValue)
        packages_installer.newInstallationLogMessage.connect(self.__log.append)
        return packages_installer

    def __create_layout(self):
        layout = QVBoxLayout(self)
        layout.addWidget(self.__progress_bar)
        layout.addWidget(self.__log)
