
from typing import Dict

from src.utils.user_validation import validate_user
from src.utils.subprocess_handler import check_exit_status_in_subprocess
from src.utils.message_displayer import fail_message, success_message

GSETTINGS_CONFIG_FORMAT = Dict[str, Dict[str, str]] 

def set_gsettings(gsettings_configuration: GSETTINGS_CONFIG_FORMAT):
    """
    Gsettings config installer
    Installs the gsettings configuration
    Settings can be found in the gsettings.json script in the repo path
    """
    if not validate_user("Install gsettings configuration?"):
        return


    for schema in gsettings_configuration:
        for key, value in gsettings_configuration[schema].items():
            setting = ["gsettings", "set", schema, key, value]
            setting_str = " ".join(setting)
            
            if check_exit_status_in_subprocess(setting):
                success_message(f"Succesfully set: '{setting_str}'")
            else:
                fail_message(f"Invalid config setting skipped: '{setting_str}'")