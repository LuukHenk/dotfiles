from dataclasses import dataclass

@dataclass
class Package:
    name: str
    installed: bool