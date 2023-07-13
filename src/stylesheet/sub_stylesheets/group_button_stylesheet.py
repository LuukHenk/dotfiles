from typing import Dict

from stylesheet.data_layer import keys
from stylesheet.data_layer import object_names as objects
from stylesheet.data_layer import defaults


def get_group_button_stylesheet(hover: bool = False) -> Dict[str, Dict[str, str]]:
    return {
        f"#{objects.GROUP_BUTTON}": {
            keys.BACKGROUND_COLOR: defaults.PRIMARY_COLOR,
            keys.BORDER: f"{defaults.BORDER_SIZE} solid {defaults.HOVER_BORDER_COLOR if hover else defaults.PRIMARY_COLOR}",
            keys.BORDER_RADIUS: defaults.BORDER_RADIUS,
            keys.COLOR: defaults.PRIMARY_BACKGROUND_COLOR,
            keys.HEIGHT: defaults.BUTTON_HEIGHT,
            keys.PADDING_LEFT: "10px",
            keys.PADDING_RIGHT: "10px",
        },
        f"#{objects.GROUP_BUTTON}:checked": {
            keys.BACKGROUND_COLOR: "#CCC",
            keys.BORDER: f"{defaults.BORDER_SIZE} solid #CCC",
            keys.COLOR: defaults.HOVER_BORDER_COLOR,
            keys.FONT_WEIGHT: "bold",
            keys.TEXT_DECORATION: "underline",
        },
    }
