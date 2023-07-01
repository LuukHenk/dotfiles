from enum import Enum

class Manager(str, Enum):
    APT = "apt"
    SNAP = "snap"