from dataclasses import dataclass

from package_installer.manager_enum import Manager

@dataclass
class Package:
    name:str
    manager: Manager
    version: str
    installation_command: str