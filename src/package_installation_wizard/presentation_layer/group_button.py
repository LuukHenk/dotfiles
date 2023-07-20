from PySide6.QtCore import Signal, QObject, QEvent
from PySide6.QtWidgets import QPushButton

from stylesheet.data_layer.object_names import GROUP_BUTTON
from stylesheet.stylesheets import StyleSheets


class GroupButton(QPushButton):
    groupNameClicked = Signal(str)

    def __init__(self, group_name: str, parent=None):
        super().__init__(text=group_name, parent=parent)
        self.__stylesheet_handler = StyleSheets()
        self.setObjectName(GROUP_BUTTON)
        self.setCheckable(True)
        self.clicked.connect(lambda: self.groupNameClicked.emit(group_name))
        self.installEventFilter(self)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Enter:
            self.setStyleSheet(self.__stylesheet_handler.stylesheet_on_group_button_hover)
        elif event.type() == QEvent.Leave:
            self.setStyleSheet(self.__stylesheet_handler.default_stylesheet)
        return False
