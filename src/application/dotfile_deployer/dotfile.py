from dataclasses import dataclass
from pathlib import Path

@dataclass
class Dotfile:
    name: str
    repository_path: Path
    deploy_path: Path