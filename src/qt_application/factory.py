from data_layer.package_accessor import PackageAccessor
from installation_wizard_widget.installation_wizard_widget import InstallationWizardWidget
from package_installer.installation_progress_widget.installation_progress_widget import InstallationProgressWidget
class Factory:
    def __init__(self):
        self.__package_accessor = PackageAccessor()

    def create_installation_wizard_widget(self) -> InstallationWizardWidget:
        return InstallationWizardWidget(self.__package_accessor)

    def create_installation_progress_widget(self) -> InstallationProgressWidget:
        return InstallationProgressWidget(self.__package_accessor)
