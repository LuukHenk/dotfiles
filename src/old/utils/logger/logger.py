from datetime import datetime

__WARNING_COLOR = '\033[93m'
__FAIL_COLOR = '\033[91m'
__END_COLOR = '\033[0m'

__LOG_MESSAGE_TEMPLATE = "[{}] {}"
def log_error(error_message: str) -> None:
    __publish_log_message(f"{__FAIL_COLOR}ERROR: {error_message}{__END_COLOR}")

def log_info(info_message: str) -> None:
    __publish_log_message(f"INFO: {info_message}")
def __publish_log_message(message: str) -> None:
    print(__LOG_MESSAGE_TEMPLATE.format(datetime.now(), message))
