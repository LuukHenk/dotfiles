from dataclasses import dataclass

from data_models.version_type import VersionType


@dataclass
class Version:
    type: VersionType
    name: str
