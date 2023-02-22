from typing import List

from package_installer.package import Package
from package_installer.manager_enum import Manager
from package_installer.version_enum import Version

packages: List[Package] = [
    Package(
        name="spotify",
        manager=Manager.SNAP,
        version=Version.LATEST_STABLE
    ),
    Package(
        name="pogo",
        manager=Manager.SNAP,
        version=Version.LATEST_STABLE
    ),
    Package(
        name="this is not a valid name",
        manager=Manager.SNAP,
        version=Version.LATEST_STABLE
    ),
]