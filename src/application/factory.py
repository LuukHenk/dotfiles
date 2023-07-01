from configuration_loader.configuration_loader import ConfigurationLoader
from data_layer.package_accessor import PackageAccessor
from installation_wizard_widget.business_layer.factory import Factory as InstallationWizardWidgetFactory
from installation_wizard_widget.presentation_layer.installation_wizard_widget import InstallationWizardWidget


class Factory:
    def __init__(self):
        self.__package_accessor = PackageAccessor()
        configuration_loader = ConfigurationLoader()
        configuration_loader.load_packages(self.__package_accessor)

    def create_installation_wizard_widget(self) -> InstallationWizardWidget:
        return InstallationWizardWidgetFactory(self.__package_accessor).installation_wizard_widget
