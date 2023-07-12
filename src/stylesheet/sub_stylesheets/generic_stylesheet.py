from typing import Dict

from stylesheet.data_layer import keys
from stylesheet.data_layer import object_names as objects
from stylesheet.data_layer import defaults


def get_raw_generic_stylesheet() -> Dict[str, Dict[str, str]]:
    return {
        f"#{objects.PACKAGE_FRAME}": {
            keys.BORDER: f"{defaults.BORDER_SIZE} solid {defaults.PRIMARY_COLOR}",
            keys.BORDER_RADIUS: defaults.BORDER_RADIUS,
        },
        f"#{objects.PACKAGE_FRAME_HEADER}": {
            keys.COLOR: defaults.PRIMARY_COLOR,
            keys.FONT_SIZE: "36px",
            keys.FONT_WEIGHT: "bold",
            keys.MARGIN_BOTTOM: "10px",
        },
        f"#{objects.PACKAGES_PANEL_HEADER}": {
            keys.COLOR: defaults.PRIMARY_COLOR,
            keys.FONT_SIZE: "48px",
            keys.FONT_WEIGHT: "bold",
            keys.MARGIN_BOTTOM: "10px",
        },
    }
