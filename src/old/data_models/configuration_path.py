

from enum import Enum
from pathlib import Path


class ConfigurationPath(str, Enum):
    PACKAGE_CONFIGURATION_PATH = "../etc/packages.json"