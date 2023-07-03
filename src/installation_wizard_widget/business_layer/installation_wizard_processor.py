from data_layer.package_accessor import PackageAccessor
from installation_wizard_widget.business_layer.id_tracker import IdTracker


class InstallationWizardProcessor:
    def __init__(self, package_accessor: PackageAccessor, id_tracker: IdTracker):
        self.__package_accessor = package_accessor
        self.__packages_to_install = id_tracker

    def any_selected_packages(self) -> bool:
        return bool(self.__packages_to_install.ids)

    def update_packages_to_install(self, package_id: int, install: bool):
        if install:
            self.__packages_to_install.add_id(package_id)
            return
        self.__packages_to_install.remove_id(package_id)
