
from abc import ABC, abstractmethod
from typing import List
from subprocess import run, CompletedProcess

from package_installer.data_models.package_info import PackageInfo


class PackageManagerHandler(ABC):
    @abstractmethod
    def find_package(self, package_name: str) -> List[PackageInfo]:
        pass
        
    @staticmethod
    def _run_command(command: List[str]) -> CompletedProcess:
        return run(command, capture_output=True, check=False, encoding="utf-8")