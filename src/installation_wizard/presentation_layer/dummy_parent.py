from PySide6.QtWidgets import QWidget, QHBoxLayout
from data_models.manager_name import ManagerName
from data_models.version import Version

from data_models.package import Package
from data_models.version_type import VersionType
from installation_wizard.presentation_layer.packages_panel import PackagesPanel
from installation_wizard.presentation_layer.stacked_packages_panels import StackedPackagesPanels


class DummyParent(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        layout = QHBoxLayout(self)

        packages_names = "Python"
        dummy_apt_package = Package(
            manager_name=ManagerName.APT,
            name=packages_names,
            search_name="python",
            installation_request=False,
            installed=False,
            version=Version(name="V1.0005", type=VersionType.LATEST_STABLE),
            groups=[],
        )
        dummy_snap_package = Package(
            manager_name=ManagerName.SNAP,
            name=packages_names,
            search_name="python",
            installation_request=False,
            installed=False,
            version=Version(name="V1.0005", type=VersionType.LATEST_STABLE),
            groups=[],
        )
        packages = [dummy_apt_package, dummy_snap_package]
        package_panels = StackedPackagesPanels()
        package_panels.add_group_panel("Home packages", [packages] * 20)
        layout.addWidget(package_panels)
