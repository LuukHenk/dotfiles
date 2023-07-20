from string import capwords

from PySide6.QtWidgets import QLabel

from data_models.manager_name import ManagerName
from stylesheet.data_layer.object_names import PACKAGE


class ManagerLabel(QLabel):
    def __init__(self, manager_name: ManagerName, parent=None):
        super().__init__(text=capwords(manager_name.value), parent=parent)
        self.setObjectName(f"{PACKAGE}{manager_name.value}")
        self.setFixedWidth(50)
