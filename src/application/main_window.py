from PySide6.QtCore import Signal
from PySide6.QtWidgets import QMainWindow
from installation_wizard.presentation_layer.installation_wizard_widget import InstallationWizardWidget
from installer.installing_status_widget.installation_status_widget import InstallationStatusWidget


class MainWindow(QMainWindow):
    readyForInstallation = Signal()

    def __init__(
        self,
        installation_wizard_widget: InstallationWizardWidget,
        installation_status_widget: InstallationStatusWidget,
    ):
        super().__init__()
        self.__installation_wizard_widget = installation_wizard_widget
        self.__installation_status_widget = installation_status_widget
        self.setCentralWidget(self.__installation_wizard_widget)

    def show_installation_status_widget(self):
        self.setCentralWidget(self.__installation_status_widget)
        self.readyForInstallation.emit()
