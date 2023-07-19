from dataclasses import dataclass
from pathlib import Path

from data_models.item import Item


@dataclass
class Dotfile(Item):
    repo_path: Path
    deploy_path: Path

    def __post_init__(self):
        super().__post_init__()

    def __repr__(self):
        return f"Dotfile(name={self.name}, installed={self.installed})"
