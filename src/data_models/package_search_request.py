from dataclasses import dataclass
from typing import List

@dataclass
class ParsedPackage:
    name: str
    search_query: List[str]
    package_group: str
