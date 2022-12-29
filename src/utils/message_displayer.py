"""Displays a message to the user via the terminal"""

from enum import Enum
from colorama import Fore, Style

class MessageTypes(Enum):
    SUCCESS = Fore.GREEN
    FAIL = Fore.RED
    
def fail_message(message:str):
    """Displays a fail message"""
    __display_message(message, MessageTypes.FAIL)

def success_message(message: str):
    """Displays a success message"""
    __display_message(message, MessageTypes.SUCCESS)

def __display_message(message, message_type: MessageTypes):
    print(f"{message_type.value}{message}")
    print(Style.RESET_ALL, end="")
