from dataclasses import dataclass
from typing import List

@dataclass
class PackageSearchRequest:
    name: str
    search_query: List[str]
    package_group: str
