from PySide6.QtWidgets import QWidget
from package_finder.package_finder import PackageFinder
from installation_wizard_widget.installation_wizard_widget import InstallationWizardWidget
from installation_wizard_widget.installation_wizard_widget_processor import  InstallationWizardWidgetProcessor
from package_installer.installation_progress_widget.installation_progress_widget_processor import InstallationProgressWidgetProcessor
from package_installer.installation_progress_widget.installation_progress_widget import InstallationProgressWidget
class Factory:
    def __init__(self):
        self.__packages = PackageFinder().get_package_info()

    def create_installation_wizard_widget(self) -> InstallationWizardWidget:
        installation_wizard_widget_processor = InstallationWizardWidgetProcessor(self.__packages)
        return InstallationWizardWidget(installation_wizard_widget_processor)

    def create_installation_progress_widget(self) -> InstallationProgressWidget:
        installation_process_widget_processor = InstallationProgressWidgetProcessor(self.__packages)
        return InstallationProgressWidget(installation_process_widget_processor)
