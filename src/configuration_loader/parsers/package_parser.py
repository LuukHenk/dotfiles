from tomllib import load
from pathlib import Path
from typing import List

from configuration_loader.parsers.parser import Parser
from data_models.object import Object


class PackageParser(Parser):
    def parse_toml_file(self, file_path: Path) -> List[Object]:
        with open(file_path, "rb") as f:
            package_data = load(f)
            print(package_data)
