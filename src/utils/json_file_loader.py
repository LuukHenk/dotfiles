    
from typing import Optional
from pathlib import Path
from json import loads

from src.utils.message_displayer import fail_message

    
def load_json_file(path: Path) -> Optional[any]:
    """Loads a json file from the default repo path
    Returns None if the file can't be found
    """
    try:
        with open(path, "r") as json_file:
            json_data = json_file.read()
        return loads(json_data)
    except FileNotFoundError as err:
        fail_message(err)
        return None