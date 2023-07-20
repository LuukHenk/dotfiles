from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout


class InstallationWizardWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__create_layout()
        # TODO: Create treeview widget
        # TODO: Create apply button widget
        pass

    def __create_layout(self):
        layout = QVBoxLayout(self)
        layout.addWidget(QPushButton("Apply Changes"))
