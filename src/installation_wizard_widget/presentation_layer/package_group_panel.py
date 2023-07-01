from typing import List

from PySide6.QtWidgets import QWidget

from data_models.package import Package


class PackageGroupPanel(QWidget):
    def __init__(self, group_name: str, packages: List[Package], parent=None):
        super().__init__(parent)
