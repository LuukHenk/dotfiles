from typing import Dict

from utils.root_finder import ROOT
from data_models.manager_name import ManagerName
from stylesheet.data_layer.object_names import PACKAGE_LABEL, PACKAGE_CHECKBOX, PACKAGE_VERSION, PACKAGE
from stylesheet.data_layer.defaults import (
    BORDER_RADIUS,
    PRIMARY_COLOR,
    PRIMARY_BACKGROUND_COLOR,
    HOVER_BORDER_COLOR,
    BORDER_SIZE,
    BUTTON_HEIGHT,
)
from stylesheet.data_layer import keys

APT_COLOR = "#BA4D00"
SNAP_COLOR = "#6D8764"


def get_raw_package_stylesheet(hover: bool = False) -> Dict[str, Dict[str, str]]:
    return {
        f"#{PACKAGE_LABEL}": {
            keys.BACKGROUND_COLOR: PRIMARY_COLOR,
            keys.BORDER: f"{BORDER_SIZE} solid {HOVER_BORDER_COLOR if hover else PRIMARY_COLOR}",
            keys.BORDER_RADIUS: BORDER_RADIUS,
            keys.HEIGHT: BUTTON_HEIGHT,
        },
        f"#{PACKAGE_CHECKBOX}": {
            keys.BACKGROUND_COLOR: PRIMARY_COLOR,
            keys.BORDER_RADIUS: BORDER_RADIUS,
            keys.SPACING: 0,
        },
        f"::indicator#{PACKAGE_CHECKBOX}": {
            keys.BACKGROUND_COLOR: PRIMARY_COLOR,
            keys.BORDER: f"{BORDER_SIZE} solid {HOVER_BORDER_COLOR if hover else PRIMARY_COLOR}",
            keys.BORDER_RADIUS: BORDER_RADIUS,
            keys.HEIGHT: BUTTON_HEIGHT,
            keys.WIDTH: BUTTON_HEIGHT,
        },
        f"::indicator:checked#{PACKAGE_CHECKBOX}": {
            keys.IMAGE: f"url({ROOT}/static/images/icons8-checked.svg)",
        },
        f"#{PACKAGE_VERSION}": {
            keys.BACKGROUND_COLOR: PRIMARY_COLOR,
            keys.BORDER_RADIUS: BORDER_RADIUS,
            keys.COLOR: PRIMARY_BACKGROUND_COLOR,
        },
        f"#{PACKAGE}{ManagerName.APT.value}": {
            keys.BACKGROUND_COLOR: APT_COLOR,
            keys.BORDER: f"{BORDER_SIZE} solid {HOVER_BORDER_COLOR if hover else APT_COLOR}",
            keys.BORDER_RADIUS: BORDER_RADIUS,
            keys.COLOR: PRIMARY_BACKGROUND_COLOR,
            keys.PADDING: "5px",
        },
        f"#{PACKAGE}{ManagerName.SNAP.value}": {
            keys.BACKGROUND_COLOR: SNAP_COLOR,
            keys.BORDER: f"{BORDER_SIZE} solid {HOVER_BORDER_COLOR if hover else SNAP_COLOR}",
            keys.BORDER_RADIUS: BORDER_RADIUS,
            keys.COLOR: PRIMARY_BACKGROUND_COLOR,
            keys.PADDING: "5px",
        },
    }
