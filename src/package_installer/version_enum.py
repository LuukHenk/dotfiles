from enum import Enum

class Version(str, Enum):
    STABLE = "Latest"
    CANDIDATE = "Candidate"
    BETA = "Beta"
    EDGE = "Edge"