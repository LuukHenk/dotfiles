from dataclasses import dataclass, field
from uuid import uuid4, UUID
from typing import List

from business_layer.id_generator import IdGenerator
from data_models.version import Version
from data_models.manager_name import ManagerName


@dataclass
class Package:
    version: Version  # BK
    installed: bool = field(repr=False)
    search_name: str  # BK
    manager_name: ManagerName  # BK
    name: str = field(repr=False, default="")
    groups: List[str] = field(default_factory=list, repr=False)
    installation_request: bool = field(default=False, repr=False)

    def __post_init__(self):
        self._id: int = IdGenerator().generate_id()  # PK

    @property
    def id_(self) -> int:
        return self._id

    def __str__(self) -> str:
        return f"{self.search_name} {self.version.type} {self.manager_name}"
