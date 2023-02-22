from enum import Enum

class Version(str, Enum):
    LATEST_STABLE = "Stable"
    LATEST_CANDIDATE = "Candidate"
    LATEST_BETA = "Beta"
    LATEST_EDGE = "Edge"
    OTHER = "Other"