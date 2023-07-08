from typing import Dict

from stylesheet.data_layer import keys
from stylesheet.data_layer import object_names as objects
from stylesheet.data_layer import defaults


def get_raw_generic_stylesheet() -> Dict[str, Dict[str, str]]:
    return {
        f"#{objects.PACKAGE_NAME_SET}": {
            keys.BORDER: f"{defaults.BORDER_SIZE} solid {defaults.PRIMARY_COLOR}",
            keys.BORDER_RADIUS: defaults.BORDER_RADIUS,
        },
        f"#{objects.PACKAGE_NAME_SET_HEADER}": {
            keys.COLOR: defaults.PRIMARY_COLOR,
            keys.FONT_SIZE: "36px",
            keys.FONT_WEIGHT: "bold",
            keys.MARGIN_BOTTOM: "10px",
        },
    }
