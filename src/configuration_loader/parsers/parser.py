from abc import ABC, abstractmethod
from pathlib import Path

from typing import List

from data_models.object import Object


class Parser(ABC):
    @abstractmethod
    def parse(self, file_path: Path) -> List[Object]:
        pass
