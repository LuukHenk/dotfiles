from typing import Tuple

from data_models.version import Version
from data_models.object import Object


class Package(Object):
    version: Tuple[str, Version] = ("", Version.UNKNOWN)
