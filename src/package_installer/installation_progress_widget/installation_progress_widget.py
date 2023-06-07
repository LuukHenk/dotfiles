

from PySide6.QtWidgets import QWidget

from data_layer.package_accessor import PackageAccessor

class InstallationProgressWidget(QWidget):
    def __init__(self, package_accessor: PackageAccessor, parent=None):
        super().__init__(parent)
        self.__package_accessor = package_accessor

    def show(self) -> None:
        print(self.__package_accessor.find_packages_with_an_installation_request())
        super().show()
