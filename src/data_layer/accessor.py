from dataclasses import dataclass

from data_layer.access_point.access_point import AccessPoint


@dataclass
class Accessor:
    package_accessor = AccessPoint()
