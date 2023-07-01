from dataclasses import dataclass

from data_models.manager_name import ManagerName
from data_models.version import Version


@dataclass
class PackageManagerSearchResult:
    manager_name: ManagerName
    package_version: Version
    package_installed: bool
