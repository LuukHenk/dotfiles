import dataclasses
from abc import ABC

from data_models.state import State
from old.data_models.manager import Manager


@dataclasses.dataclass
class Object(ABC):
    identifier: int
    name: str
    group: str
    search_name: str
    manager: Manager
    state: State
