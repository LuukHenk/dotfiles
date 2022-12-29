"""User validation"""


def validate_user(message: str) -> bool:
    """
    User validation
    ---
    Requests user input. If the user ansers with 'y' or 'yes', the function will return
    True. 
    """
    return input(f"-- {message} [y/N]").lower() in ["y", "yes"]