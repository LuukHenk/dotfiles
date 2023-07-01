from enum import Enum


class AccessorResultMessage(str, Enum):
    DUPLICATION = "Found a duplication in the 'search_names' column of '{}' and '{}'. search_names must be unique."
    UNCHANGED = "The updated object is unchanged."
    NOT_FOUND = "Object not found."
