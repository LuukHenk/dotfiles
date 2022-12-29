""" The main window of our application"""

from sys import argv, exit as sys_exit
from PySide6.QtWidgets import QApplication, QMainWindow

from src.application.application import Application


class MainWindow(QMainWindow):
    """The main window of the 2048 game"""

    def __init__(self):
        super().__init__()
        self.__application = Application()
        self.setCentralWidget(self.__application.application_widget)


def run_main_window():
    """Runs the main window, kills everything that is in the main window when closed"""
    app = QApplication(argv)
    window = MainWindow()
    window.show()

    sys_exit(app.exec())

if __name__ == "__main__":
    run_main_window()