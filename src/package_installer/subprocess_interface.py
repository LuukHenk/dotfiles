
from typing import List
from subprocess import run, CompletedProcess

@staticmethod
def run_(command: List[str]) -> CompletedProcess:
    return run(command, capture_output=True, check=False, encoding="utf-8")