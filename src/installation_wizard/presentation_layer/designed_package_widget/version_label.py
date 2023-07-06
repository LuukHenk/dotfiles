from PySide6.QtWidgets import QLabel


class VersionLabel(QLabel):
    def __init__(self, version_text: str, parent=None):
        super().__init__(text=version_text, parent=parent)
