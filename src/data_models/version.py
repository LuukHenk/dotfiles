from dataclasses import dataclass, field

from data_models.version_type import VersionType


@dataclass
class Version:
    type: VersionType
    name: str = field(repr=False)
