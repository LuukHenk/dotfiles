PACKAGE_WIDGET_NAME = "package_widget"
PACKAGE_LABEL_NAME = "package_label"
VERSION_LABEL_NAME = "version_label"

__DEFAULT_BACKGROUND_COLOR = "#DEDDDA"
__DEFAULT_HEIGHT = "33px"
__DEFAULT_BORDER_RADIUS = "10px"

__HOVER_BORDER_COLOR = "#3584E4"

DEFAULT_STYLE = f"""

    QWidget#{PACKAGE_LABEL_NAME} {{
        border-radius: {__DEFAULT_BORDER_RADIUS};
        height: {__DEFAULT_HEIGHT};
        background-color: {__DEFAULT_BACKGROUND_COLOR};
        border: 2px solid {__DEFAULT_BACKGROUND_COLOR};
    }}
    QCheckBox {{
        spacing: 0px;
        border-radius: {__DEFAULT_BORDER_RADIUS};
        background-color: {__DEFAULT_BACKGROUND_COLOR};
    }}
    QCheckBox::indicator {{
        height: {__DEFAULT_HEIGHT};
        width: {__DEFAULT_HEIGHT};
        border-radius: {__DEFAULT_BORDER_RADIUS};
        background-color: {__DEFAULT_BACKGROUND_COLOR};
        border: 2px solid {__DEFAULT_BACKGROUND_COLOR};
    }}
    QCheckBox::indicator:checked {{
        image: url(../static/images/icons8-checked.svg)
    }}
    QLabel#{VERSION_LABEL_NAME} {{
        margin-left: 2px;
        color: #000000;
        padding:5px;
        border-radius: {__DEFAULT_BORDER_RADIUS};
        background-color: {__DEFAULT_BACKGROUND_COLOR};
    }}
    QLabel#apt {{
        background-color: #BA4D00;
        border: 2px solid #BA4D00;
        color: #000000;
        padding:5px;
        border-radius: {__DEFAULT_BORDER_RADIUS};
    }}
    QLabel#snap {{
        background-color: #6D8764;
        border: 2px solid #6D8764;
        color: #000000;
        padding:5px;
        border-radius: {__DEFAULT_BORDER_RADIUS};
    }}
"""
HOVER_STYLE = f"""
    QWidget#{PACKAGE_LABEL_NAME} {{
        color: #000000;
        border-radius: {__DEFAULT_BORDER_RADIUS};
        height: {__DEFAULT_HEIGHT};
        background-color: {__DEFAULT_BACKGROUND_COLOR};
        border: 2px solid {__HOVER_BORDER_COLOR};
    }}
    
    QCheckBox {{
        spacing: 0px;
        border-radius: {__DEFAULT_BORDER_RADIUS};
        background-color: {__DEFAULT_BACKGROUND_COLOR};
    }}
    QCheckBox::indicator {{
        height: {__DEFAULT_HEIGHT};
        width: {__DEFAULT_HEIGHT};
        border-radius: {__DEFAULT_BORDER_RADIUS};
        background-color: {__DEFAULT_BACKGROUND_COLOR};
        border: 2px solid {__HOVER_BORDER_COLOR};
    }}
    QCheckBox::indicator:checked {{
        image: url(../static/images/icons8-checked.svg)
    }}
    QLabel#{VERSION_LABEL_NAME} {{
        background-color: {__DEFAULT_BACKGROUND_COLOR};
        border-radius: 0px;
        border-right: 2px solid {__DEFAULT_BACKGROUND_COLOR};
        border-left: 2px solid {__DEFAULT_BACKGROUND_COLOR};
        border-top: 2px solid {__HOVER_BORDER_COLOR};
        border-bottom: 2px solid {__HOVER_BORDER_COLOR};
        color: #000000;
        padding:5px;
    }}
    QLabel#apt {{
        background:#BA4D00;
        color: #000000;
        padding:5px;
        border: 2px solid {__HOVER_BORDER_COLOR};
        border-radius: {__DEFAULT_BORDER_RADIUS};
    }}
    QLabel#snap {{
        background:#6D8764;
        color: #000000;
        padding:5px;
        border: 2px solid {__HOVER_BORDER_COLOR};
        border-radius: {__DEFAULT_BORDER_RADIUS};
    }}
"""
