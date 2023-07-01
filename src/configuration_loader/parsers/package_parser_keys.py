from enum import Enum


class PackageParserKeys(str, Enum):
    PACKAGE_GROUPS = "package_groups"
    NAME = "name"
    PACKAGES = "packages"
    SEARCH_NAMES = "search_names"
