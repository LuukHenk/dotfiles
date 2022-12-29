
from typing import List
from PySide6.QtWidgets import QWidget, QVBoxLayout, QCheckBox


class PackageInstallerWidget(QWidget):
    def __init__(self, package_names: List[str]) -> None:
        super().__init__()

        layout = QVBoxLayout()
        for package_name in package_names:
            print(package_name)
            layout.addWidget(QCheckBox(package_name))

        self.setLayout(layout)