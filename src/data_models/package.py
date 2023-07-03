from dataclasses import dataclass, field
from uuid import uuid4, UUID
from typing import List

from business_layer.id_generator import IdGenerator
from data_models.version import Version
from data_models.manager_name import ManagerName


@dataclass
class Package:
    version: Version  # BL
    installed: bool
    search_name: str  # BK
    manager_name: ManagerName  # BK
    name: str = ""
    groups: List[str] = field(default_factory=list)

    def __post_init__(self):
        self._id: int = IdGenerator().generate_id()  # PK

    @property
    def id_(self) -> int:
        return self._id
