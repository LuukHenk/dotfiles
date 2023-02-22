from typing import List

from package_installer.package_to_install import PackageToInstall
from package_installer.manager_enum import Manager


packages: List[PackageToInstall] = [
    PackageToInstall(
        possible_package_names=["python"],
        accepted_managers=[Manager.APT],
        accepted_versions=["3.10.6"]
    )
]