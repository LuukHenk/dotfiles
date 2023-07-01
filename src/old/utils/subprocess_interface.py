from typing import List
from subprocess import run, CompletedProcess


def run_(command: List[str]) -> CompletedProcess:
    return run(command, capture_output=True, encoding="utf-8")
