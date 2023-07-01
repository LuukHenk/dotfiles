from data_models.version import Version
from data_models.object import Object


class Package(Object):
    version: Version  # BL
    installed: bool
