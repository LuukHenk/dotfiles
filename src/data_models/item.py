from abc import ABC
from dataclasses import dataclass

from business_layer.id_generator import IdGenerator


@dataclass
class Item(ABC):
    installed: bool
    name: str
    group: str

    def __post_init__(self):
        self._id: int = IdGenerator().generate_id()  # PK

    @property
    def id_(self) -> int:
        return self._id

    def __repr__(self):
        return f"Item(group={self.group})"
