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
from PySide6.QtCore import Qt, QFile, QEvent, QObject


class SomeParentWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        layout = QHBoxLayout(self)
        package = PackageWidget()
        layout.addWidget(package)


DEFAULT_HEIGHT = 35
DEFAULT_BACKGROUND = "#DEDDDA"
DEFAULT_COLOR = "#000000"
SNAP_BACKGROUND = "#6D8764"
APT_BACKGROUND = "#BA4D00"


class PackageWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.__checkbox = self.__create_checkbox()
        self.__button = PackageButtonWidget()
        self.__create_layout()
        self.setObjectName("designed_package_widget")
        self.installEventFilter(self)

    def __create_layout(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)
        layout.addWidget(self.__checkbox, alignment=Qt.AlignLeft)
        layout.addWidget(self.__button, alignment=Qt.AlignLeft)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Enter:
            return False
        if event.type() == QEvent.Leave:
            return False
        return False

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
        self.setFixedSize(self.__BUTTON_WIDTH, DEFAULT_HEIGHT)

    def __create_layout(self):
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.__create_installation_label())
        layout.addWidget(self.__create_manager_label(), alignment=Qt.AlignRight)

    def __create_installation_label(self) -> QLabel:
        label = QLabel("Install V1.005")
        label.setObjectName("Install")
        width = self.__BUTTON_WIDTH - self.__MANAGER_WIDTH
        label.setFixedSize(width, DEFAULT_HEIGHT)
        return label

    def __create_manager_label(self) -> QLabel:
        manager_name = "Apt"

        label = QLabel(manager_name)
        label.setStyleSheet("background=")
        label.setFixedSize(self.__MANAGER_WIDTH, DEFAULT_HEIGHT)
        return label


class ManagerLabel(QLabel):
    def __init__(self, manager: str, parent=None):
        super().__init__(parent=parent)


def __open_stylesheet() -> str:
    with open("style.qss", "r", encoding="UTF-8") as stylesheet_file:
        stylesheet = stylesheet_file.read()
    return stylesheet


if __name__ == "__main__":
    qt_app = QApplication(argv)
    qt_app.setStyleSheet(__open_stylesheet())
    main_app = SomeParentWidget()
    main_app.show()
    sys_exit(qt_app.exec())
