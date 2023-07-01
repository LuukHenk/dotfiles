from sys import argv, exit as sys_exit
from PySide6.QtWidgets import QApplication
from application.factory import Factory


def run_application():
    app = QApplication(argv)
    factory = Factory()
    installation_wizard_widget = factory.create_installation_wizard_widget()
    installation_wizard_widget.show()
    sys_exit(app.exec_())
