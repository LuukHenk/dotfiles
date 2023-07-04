from typing import List
from subprocess import run, CompletedProcess
import asyncio


def run_(command: List[str]) -> CompletedProcess:
    return run(command, capture_output=True, encoding="utf-8")


def run_async(command: List[str]) -> ...:
    asyncio.run(__execute_command(command))


async def __execute_command(command: List[str]) -> None:
    await asyncio.sleep(3)
    print(f"Executed {command}")
