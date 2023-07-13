from PySide6.QtCore import Signal, QObject, QEvent
from PySide6.QtWidgets import QPushButton

from stylesheet.data_layer.object_names import APPLY_BUTTON
from stylesheet.stylesheets import StyleSheets


class ApplyButton(QPushButton):
    showConfirmationButton = Signal()

    def __init__(self, parent=None):
        super().__init__(text="   Apply changes   ", parent=parent)
        self.__stylesheet_handler = StyleSheets()
        self.setObjectName(APPLY_BUTTON)
        self.setDisabled(True)
        self.installEventFilter(self)

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == QEvent.Enter:
            self.setStyleSheet(self.__stylesheet_handler.stylesheet_on_apply_button_hover)
        elif event.type() == QEvent.Leave:
            self.setStyleSheet(self.__stylesheet_handler.default_stylesheet)
        return False
