from dataclasses import dataclass
from typing import List

@dataclass
class PackageSearchQuery:
    name: str
    search_query: List[str]