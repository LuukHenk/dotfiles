

from enum import Enum
from pathlib import Path


class ConfigurationPath(Path, Enum):
    PACKAGE_CONFIGURATION_PATH = Path("../etc/packages.json")