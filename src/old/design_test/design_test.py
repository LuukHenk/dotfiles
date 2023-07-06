

from sys import argv, exit as sys_exit


from PySide6.QtWidgets import (
    QPushButton,
    QApplication,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QWidget,
    QCheckBox,
)
from PySide6.QtCore import Qt, QFile


class SomeParentWidget(QWidget):


    def __init__(self, parent=None):
        super().__init__(parent=parent)
        layout = QHBoxLayout(self)
        layout.addWidget(PackageWidget())



PACKAGE_WIDGET_HEIGHT = 35

class PackageWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__create_layout()
        self.setObjectName("package_widget")
        self.setFixedHeight(PACKAGE_WIDGET_HEIGHT)
        self.setSizePolicy(QSizePolicy.MinimumExpanding,QSizePolicy.MinimumExpanding)

    def __create_layout(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        layout.addWidget(self.__create_checkbox())
        layout.addWidget(PackageButtonWidget())

    @staticmethod
    def __create_checkbox() -> QCheckBox:
        checkbox = QCheckBox()
        checkbox.setObjectName("PackageCheckBox")
        return checkbox

class PackageButtonWidget(QPushButton):

    __BUTTON_WIDTH = 200
    __MANAGER_WIDTH = 50

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__create_layout()
        self.setObjectName("package_button_widget")
        self.setFixedSize(self.__BUTTON_WIDTH, PACKAGE_WIDGET_HEIGHT)

    def __create_layout(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.__create_installation_label())
        layout.addWidget(self.__create_manager_label(), alignment=Qt.AlignRight)

    def __create_installation_label(self) -> QLabel:
        label = QLabel("Install V1.005")
        label.setObjectName("Install")
        width=self.__BUTTON_WIDTH-self.__MANAGER_WIDTH
        label.setFixedSize(width, PACKAGE_WIDGET_HEIGHT)
        return label

    def __create_manager_label(self) -> QLabel:
        manager_name = "Snap"
        label = QLabel(manager_name)
        label.setObjectName(manager_name)
        label.setFixedSize(self.__MANAGER_WIDTH, PACKAGE_WIDGET_HEIGHT)
        return label

def __open_stylesheet() -> str:
    with open("style.qss", "r", encoding="UTF-8") as stylesheet_file:
        stylesheet = stylesheet_file.read()
    return stylesheet

if __name__ == "__main__":
    qt_app = QApplication(argv)
    qt_app.setStyleSheet(__open_stylesheet())
    main_app = PackageWidget()
    main_app.show()
    sys_exit(qt_app.exec())

