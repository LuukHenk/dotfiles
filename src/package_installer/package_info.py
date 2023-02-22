
from dataclasses import dataclass

@dataclass
class PackageInfo:
    name: str
    found: bool
    installed: bool