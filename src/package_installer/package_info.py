
from typing import Tuple, Optional
from dataclasses import dataclass

from package_installer.version_enum import Version

@dataclass
class PackageInfo:
    name: str
    found: bool = False
    installed: bool = False
    installed_version: Optional[Tuple[Version, str]] = None