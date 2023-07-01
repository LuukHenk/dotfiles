from old.data_layer.package_accessor import PackageAccessor
from old.installation_wizard_widget.installation_wizard_widget import InstallationWizardWidget
from old.package_finder import PackagesFinder
from old.package_finder import PackageSearchRequestParser
from old.package_installer.installation_progress_widget.installation_progress_widget import InstallationProgressWidget
from old.package_installer.packages_installer import PackagesInstaller


class Factory:
    def __init__(self):
        self.__package_accessor = self.__construct_package_accessor()

    def create_installation_wizard_widget(self) -> InstallationWizardWidget:
        return InstallationWizardWidget(self.__package_accessor)

    def create_installation_progress_widget(self) -> InstallationProgressWidget:
        packages_installer = PackagesInstaller(self.__package_accessor)
        return InstallationProgressWidget(packages_installer)

    @staticmethod
    def __construct_package_accessor() -> PackageAccessor:
        package_search_request_parser = PackageSearchRequestParser()
        packages_info = PackagesFinder().get_packages_info(package_search_request_parser.package_search_requests)
        return PackageAccessor(packages_info)
