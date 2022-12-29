from typing import List

from subprocess import run, CalledProcessError
    
def check_exit_status_in_subprocess(args: List[str], capture_output: bool=False) -> bool:
    """Checks the exit status for a subprocess
    Returns False if the subprocess has a non-zero exit
    """
    try:
        run(args, check=True, capture_output=True)
    except CalledProcessError:
        return False
    return True