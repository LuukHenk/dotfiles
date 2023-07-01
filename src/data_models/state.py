from enum import Enum, auto


class State(Enum):
    INSTALLED = auto()
    NOT_INSTALLED = auto()
    NOT_FOUND = auto()
    UNKNOWN = auto()
