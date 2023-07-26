from PySide6.QtCore import Signal
from PySide6.QtWidgets import QStackedWidget
from package_installation_wizard.presentation_layer.installation_wizard_widget import InstallationWizardWidget
from installer.installing_status_widget.installation_status_widget import InstallationStatusWidget


class MainWindow(QStackedWidget):
    readyForInstallation = Signal()

    def __init__(
        self,
        installation_wizard_widget: InstallationWizardWidget,
        installation_status_widget: InstallationStatusWidget,
        parent=None,
    ):
        super().__init__(parent=parent)
        self.setMinimumSize(500, 500)
        self.__installation_wizard_widget = installation_wizard_widget
        self.__installation_status_widget = installation_status_widget
        self.addWidget(self.__installation_wizard_widget)
        self.addWidget(self.__installation_status_widget)
        self.setCurrentWidget(self.__installation_wizard_widget)

    def show_installation_status_widget(self):
        self.setCurrentWidget(self.__installation_status_widget)
        self.readyForInstallation.emit()
