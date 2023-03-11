from typing import Tuple
from dataclasses import dataclass
from data_models.manager import Manager
from data_models.version import Version

@dataclass
class PackageInfo:
    name: str
    version: Tuple[str, Version]
    installed: bool
    manager: Manager