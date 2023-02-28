from typing import Tuple
from dataclasses import dataclass
from package_installer.data_models.manager_enum import ManagerEnum
from package_installer.data_models.version_enum import Version

@dataclass
class PackageInfo:
    name: str
    version: Tuple[str, Version]
    installed: bool
    manager: ManagerEnum