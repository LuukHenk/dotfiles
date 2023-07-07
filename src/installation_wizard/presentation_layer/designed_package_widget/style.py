PACKAGE_WIDGET_NAME = "package_widget"
PACKAGE_LABEL_NAME = "package_label"
VERSION_LABEL_NAME = "version_label"

__DEFAULT_BACKGROUND_COLOR = "#DEDDDA"
__DEFAULT_HEIGHT = "33px"
__DEFAULT_BORDER_RADIUS = "10px"

__HOVER_BACKGROUND_COLOR = "#999896"
__HOVER_BORDER_COLOR = "#3584E4"

DEFAULT_STYLE = f"""
    QWidget {{
        color: #000000;
        border-radius: {__DEFAULT_BORDER_RADIUS};
        height: {__DEFAULT_HEIGHT};
        background-color: {__DEFAULT_BACKGROUND_COLOR};
        border: 2px solid {__DEFAULT_BACKGROUND_COLOR};
    }}
    QCheckBox {{
        spacing: 0px;
    }}
    QCheckBox::indicator {{
        height: {__DEFAULT_HEIGHT};
        width: {__DEFAULT_HEIGHT};
        border-radius: {__DEFAULT_BORDER_RADIUS};
        background-color: {__DEFAULT_BACKGROUND_COLOR};
    }}
    QLabel {{
        padding:5px;
    }}
    QLabel#apt {{
        background:#BA4D00;
        border: 2px solid #BA4D00;
    }}
    QLabel#snap {{
        background:#6D8764;
        border: 2px solid #6D8764;
    }}
"""
HOVER_STYLE = f"""
    QWidget {{
        color: #000000;
        border-radius: {__DEFAULT_BORDER_RADIUS};
        height: {__DEFAULT_HEIGHT};
        background-color: {__DEFAULT_BACKGROUND_COLOR};
    }}
    QWidget#{PACKAGE_LABEL_NAME} {{
        background-color: {__HOVER_BACKGROUND_COLOR};
        border: 2px solid {__HOVER_BORDER_COLOR};
    }}
    
    QCheckBox {{
        spacing: 0px;
    }}
    QCheckBox::indicator {{
        height: {__DEFAULT_HEIGHT};
        width: {__DEFAULT_HEIGHT};
        border-radius: {__DEFAULT_BORDER_RADIUS};
        background-color: {__HOVER_BACKGROUND_COLOR};
        border: 2px solid {__HOVER_BORDER_COLOR};
    }}
    QLabel {{
        padding:5px;
        border-top: 2px solid {__HOVER_BORDER_COLOR};
        border-bottom: 2px solid {__HOVER_BORDER_COLOR};
        border-right: 2px solid {__HOVER_BORDER_COLOR};
        margin-left: 2px;
    }}
    QLabel#{VERSION_LABEL_NAME} {{
        background-color: {__HOVER_BACKGROUND_COLOR};
        border-radius: 0px;
        border-right: 2px solid {__HOVER_BACKGROUND_COLOR};
    }}
    QLabel#apt {{
        background:#8F3B00;
    }}
    QLabel#snap {{
        background:#52664C;
    }}
"""
