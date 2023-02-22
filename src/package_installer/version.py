from enum import Enum

class Version(str, Enum):
    STABLE = "Latest"
    BETA = "Beta"
    EDGE = "Edge"