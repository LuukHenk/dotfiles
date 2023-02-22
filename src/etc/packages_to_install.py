from typing import List

from package_installer.package import Package
from package_installer.manager_enum import Manager
from package_installer.version_enum import Version

packages: List[Package] = [
    Package(
        name="python3",
        manager=Manager.APT,
        version=Version.LATEST_STABLE
    ),
    Package(
        name="htop",
        manager=Manager.APT,
        version=Version.LATEST_STABLE
    ),
    Package(
        name="this is not a valid name",
        manager=Manager.APT,
        version=Version.LATEST_STABLE
    ),
]