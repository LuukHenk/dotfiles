
from typing import List
from src.utils.subprocess_handler import check_exit_status_in_subprocess
from src.utils.message_displayer import success_message, fail_message
from src.utils.user_validation import validate_user


def display_installed_packages(packages: List[str]):
    """
    Checks if the given packages are installed by checking the
    save location

    Arguments:
        packages (list): list of package names
    """
    if not validate_user("Check if apt packages are installed?"):
        return

    for package in packages:
        subprocess_args = ["which", package]
        if check_exit_status_in_subprocess(subprocess_args, capture_output=True):
            success_message(f"Package {package} is installed")
        else:
            fail_message(f"Package {package} is not installed")

