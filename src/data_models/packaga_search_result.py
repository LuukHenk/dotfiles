from typing import Tuple
from dataclasses import dataclass
from data_models.version import Version


@dataclass
class PackageSearchResult:
    request: str
    found_version: Tuple[str, Version]
    installed: bool
