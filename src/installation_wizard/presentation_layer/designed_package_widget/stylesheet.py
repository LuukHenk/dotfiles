DEFAULT_BACKGROUND_COLOR = "grey"
__DEFAULT_HEIGHT = "35px"
__DEFAULT_BORDER_RADIUS = "10px"
__SNAP_BACKGROUND = "#6D8764"
__APT_BACKGROUND = "#BA4D00"


PACKAGE_WIDGET_STYLESHEET = f"""
    QWidget {{
        color: #000000;
        border-radius: {__DEFAULT_BORDER_RADIUS};
        background-color: {DEFAULT_BACKGROUND_COLOR};
        height: {__DEFAULT_HEIGHT};
    }}
"""
CHECKBOX_STYLESHEET = f"""
    QCheckBox::indicator {{
        height: {__DEFAULT_HEIGHT};
        width: {__DEFAULT_HEIGHT};
        background-color: {DEFAULT_BACKGROUND_COLOR};
        border-radius: {__DEFAULT_BORDER_RADIUS};
    }}
    QCheckBox {{
        spacing: 0px;
    }}
"""

MANAGER_LABEL_STYLESHEET = """
    QLabel {{
        background:{};
        padding:5px;
    }}
"""
