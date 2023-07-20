from typing import List

from PySide6.QtCore import Signal, QObject

from data_models.item import Item
from installation_wizard.business_layer.config_formatter import format_config


class InstallationWizard(QObject):
    install = Signal()

    def __init__(self, config: List[Item], parent=None) -> None:
        super().__init__(parent)
        formatted_config = format_config(config)
