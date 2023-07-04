from typing import List
from subprocess import run, CompletedProcess
import asyncio

from data_models.result import Result


def run_(command: List[str]) -> CompletedProcess:
    return run(command, capture_output=True, encoding="utf-8")


def run_async(command: List[str]) -> Result:
    return asyncio.run(__execute_command(command))


async def __execute_command(command: List[str]) -> Result:
    await asyncio.sleep(3)
    return Result(success=False, message=f"{command}")
