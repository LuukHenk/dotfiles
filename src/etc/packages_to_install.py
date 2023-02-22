from typing import List

from package_installer.package import Package
from package_installer.manager_enum import Manager
from package_installer.version import Version

packages: List[Package] = [
    Package(
        name="spotify",
        manager=Manager.SNAP,
        version=Version.STABLE
    )
]