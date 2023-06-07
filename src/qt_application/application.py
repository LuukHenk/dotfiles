import time
from sys import argv, exit as sys_exit
from PySide6.QtWidgets import QApplication
from qt_application.factory import Factory




def run_application():
    app = QApplication(argv)
    factory = Factory()
    installation_wizard_widget = factory.create_installation_wizard_widget()
    installation_progress_widget = factory.create_installation_progress_widget()

    installation_wizard_widget.install.connect(installation_progress_widget.show)
    installation_wizard_widget.show()

    sys_exit(app.exec_())
