from typing import List

from package_installer.package import Package
from package_installer.manager_enum import Manager
from package_installer.version_enum import Version

packages: List[Package] = [
    Package(
        name="spotifyf",
        manager=Manager.SNAP,
        version=Version.STABLE
    )
]