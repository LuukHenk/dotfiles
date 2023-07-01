from enum import Enum


class AccessorResultMessage(str, Enum):
    DUPLICATION = "Duplication error. Search name with manager must be unique."
    UNCHANGED = "The updated object is unchanged."
    NOT_FOUND = "Object not found."
