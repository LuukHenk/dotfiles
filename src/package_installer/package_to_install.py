from typing import List
from dataclasses import dataclass
from package_installer.manager_enum import Manager

@dataclass
class PackageToInstall:
    """NOTE that the lists are ordered, with the most prefered option first"""
    possible_package_names: List[str]
    accepted_versions: List[str]
    accepted_managers: List[Manager]