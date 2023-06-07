

from PySide6.QtWidgets import QWidget
from package_installer.installation_progress_widget.installation_progress_widget_processor import InstallationProgressWidgetProcessor

class InstallationProgressWidget(QWidget):
    def __init__(self, processor: InstallationProgressWidgetProcessor, parent=None):
        super().__init__(parent)
        self.__processor = processor

    def show(self) -> None:
        print("hi")
        super().show()
