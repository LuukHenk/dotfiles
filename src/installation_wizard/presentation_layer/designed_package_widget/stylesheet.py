DEFAULT_BACKGROUND_COLOR = "grey"
__HOVER_BACKGROUND_COLOR = "white"
__HOVER_BORDER_COLOR = "black"
__DEFAULT_HEIGHT = "35px"
__DEFAULT_BORDER_RADIUS = "10px"
__SNAP_BACKGROUND = "#6D8764"
__APT_BACKGROUND = "#BA4D00"

MANAGER_LABEL_STYLESHEET = """
    QLabel {{
        background:{};
        padding:5px;
    }}
"""

PACKAGE_WIDGET_STYLESHEET = f"""
    QWidget {{
        color: #000000;
        border-radius: {__DEFAULT_BORDER_RADIUS};
        height: {__DEFAULT_HEIGHT};
        background-color: {DEFAULT_BACKGROUND_COLOR};
    }}
"""

__CHECKBOX_STYLESHEET_TEMPLATE = f"""
    QCheckBox {{
        spacing: 0px;
    }}
    QCheckBox::indicator {{
        height: {__DEFAULT_HEIGHT};
        width: {__DEFAULT_HEIGHT};
        border-radius: {__DEFAULT_BORDER_RADIUS};
"""
__LABEL_STYLESHEET_TEMPLATE = """
    QWidget {
"""


def __get_default_stylesheet(template: str) -> str:
    template += f"""
        background-color: {DEFAULT_BACKGROUND_COLOR};
    }}
    """
    return template


def __get_stylesheet_on_hover(template: str) -> str:
    template += f"""
        background-color: {__HOVER_BACKGROUND_COLOR};
    }}
    """
    return template


def get_default_checkbox_stylesheet() -> str:
    return __get_default_stylesheet(__CHECKBOX_STYLESHEET_TEMPLATE)


def get_checkbox_stylesheet_on_hover() -> str:
    return __get_stylesheet_on_hover(__CHECKBOX_STYLESHEET_TEMPLATE)


def get_default_version_label_stylesheet() -> str:
    return __get_default_stylesheet(__LABEL_STYLESHEET_TEMPLATE)


def get_version_label_stylesheet_on_hover() -> str:
    return __get_stylesheet_on_hover(__LABEL_STYLESHEET_TEMPLATE)
