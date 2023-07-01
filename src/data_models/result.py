import dataclasses


@dataclasses.dataclass
class Result:
    success: bool
    message: str = ""
