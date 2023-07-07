from typing import List
from subprocess import run, CompletedProcess, PIPE
import asyncio

from data_models.result import Result


def run_(command: List[str]) -> CompletedProcess:
    return run(command, capture_output=True, encoding="utf-8")


def run_async_command(command: str) -> Result:
    return asyncio.run(__execute_command(command))


async def __execute_command(command: str) -> Result:
    process = await asyncio.create_subprocess_shell(command, stdout=PIPE, stderr=PIPE)
    await process.wait()
    std_out, std_err = await process.communicate()
    if process.returncode == 0:
        return Result(success=True, message=std_out.decode("utf-8"))
    return Result(success=False, message=std_err.decode("utf-8"))
