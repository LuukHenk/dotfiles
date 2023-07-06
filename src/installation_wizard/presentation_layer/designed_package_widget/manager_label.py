from string import capwords

from PySide6.QtWidgets import QLabel
from data_models.manager_name import ManagerName
from installation_wizard.presentation_layer.designed_package_widget.stylesheet import (
    DEFAULT_BACKGROUND_COLOR,
    MANAGER_LABEL_STYLESHEET,
)


class ManagerLabel(QLabel):
    def __init__(self, manager_name: ManagerName, parent=None):
        super().__init__(text=capwords(manager_name.value), parent=parent)
        self.__set_stylesheet(manager_name)

    def __set_stylesheet(self, manager_name: ManagerName):
        background_color = self.__get_manager_background_color(manager_name)
        stylesheet = MANAGER_LABEL_STYLESHEET.format(background_color)
        self.setStyleSheet(stylesheet)
        self.setFixedWidth(50)

    @staticmethod
    def __get_manager_background_color(manager_name: ManagerName) -> str:
        match manager_name:
            case ManagerName.APT:
                return "#BA4D00"
            case ManagerName.SNAP:
                return "#6D8764"
            case _:
                return DEFAULT_BACKGROUND_COLOR
