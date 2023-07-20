from dataclasses import dataclass

from data_models.version import Version

from data_models.manager_name import ManagerName

from data_models.item import Item


@dataclass
class Package(Item):
    version: Version
    search_name: str
    manager_name: ManagerName

    def __post_init__(self):
        super().__post_init__()
