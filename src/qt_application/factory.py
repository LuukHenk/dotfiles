from data_layer.package_accessor import PackageAccessor
from installation_wizard_widget.installation_wizard_widget import InstallationWizardWidget
from package_finder.package_finder import PackageFinder
from package_finder.package_search_request_parser import PackageSearchRequestParser
from package_installer.installation_progress_widget.installation_progress_widget import InstallationProgressWidget
from package_installer.packages_installer import PackagesInstaller


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
        package_groups = PackageFinder().get_package_info(package_search_request_parser.package_search_requests)
        return PackageAccessor(package_groups)
