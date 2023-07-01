from enum import Enum


class PackageParserKeys(str, Enum):
    GROUPS = "groups"
    NAME = "name"
    PACKAGES = "packages"
    SEARCH_NAMES = "search_names"
