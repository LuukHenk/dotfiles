import dataclasses
from uuid import uuid4, UUID

from data_models.state import State
from old.data_models.manager import Manager


@dataclasses.dataclass
class Object:
    search_name: str  # BK
    manager: Manager  # BK
    name: str = ""
    group: str = ""
    state: State = State.UNKNOWN

    def update(self, **kwargs):  # TODO: #0000001
        for key, value in kwargs.items():
            if key == "_id":
                continue
            if hasattr(self, key):
                setattr(self, key, value)

    def __post_init__(self):
        self._id: UUID = uuid4()  # PK

    @property
    def id_(self) -> int:
        return self._id.int
