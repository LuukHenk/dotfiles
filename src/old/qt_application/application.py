from sys import argv, exit as sys_exit
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QObject
from old.qt_application.factory import Factory


def run_application():
    app = QApplication(argv)
    _main_object = MainObject()
    sys_exit(app.exec_())


class MainObject(QObject):
    def __init__(self, parent=None):
        factory = Factory()
        self.__installation_wizard_widget = factory.create_installation_wizard_widget()
        self.__installation_progress_widget = factory.create_installation_progress_widget()
        self.__installation_wizard_widget.install.connect(self.__installation_progress_widget.show)
        self.__installation_wizard_widget.show()
        super().__init__(parent)
