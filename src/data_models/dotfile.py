from dataclasses import dataclass
from pathlib import Path

from data_models.item import Item


@dataclass
class Dotfile(Item):
    repo_path: Path
    deploy_path: Path

    def __post_init__(self):
        super().__post_init__()
