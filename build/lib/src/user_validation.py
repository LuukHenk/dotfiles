"""User validation"""


def validate(message: str) -> bool:
    """
    User validation
    ---
    Requests user input. If the user ansers with 'y' or 'yes', the function will return
    True. 
    """
    answer = input(f"-- {message} [y/N]")
    if answer.lower() not in ["y", "yes"]:
        return True
    return False