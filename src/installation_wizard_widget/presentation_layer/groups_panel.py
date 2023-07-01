from typing import List

from PySide6.QtWidgets import QWidget


class GroupsPanel(QWidget):
    def __init__(self, group_names: List[str], parent=None):
        super().__init__(parent)
