from typing import Dict

from stylesheet.data_layer import keys
from stylesheet.data_layer import object_names as objects
from stylesheet.data_layer import defaults


def get_apply_button_stylesheet(hover: bool = False) -> Dict[str, Dict[str, str]]:
    return {
        f"#{objects.APPLY_BUTTON}": {
            keys.BACKGROUND_COLOR: defaults.PRIMARY_COLOR,
            keys.BORDER: f"{defaults.BORDER_SIZE} solid {defaults.HOVER_BORDER_COLOR if hover else defaults.PRIMARY_COLOR}",
            keys.BORDER_RADIUS: defaults.BORDER_RADIUS,
            keys.COLOR: defaults.PRIMARY_BACKGROUND_COLOR,
            keys.HEIGHT: defaults.BUTTON_HEIGHT,
        },
        f"#{objects.APPLY_BUTTON}:disabled": {
            keys.BORDER: f"{defaults.BORDER_SIZE} solid {defaults.PRIMARY_COLOR}",
            keys.COLOR: defaults.DISABLE_COLOR,
        },
    }
