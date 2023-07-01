from configuration_loader.configuration_loader import ConfigurationLoader
from data_layer.accessor import Accessor


class Factory:
    def __init__(self):
        self.__accessor = Accessor()
        configuration_loader = ConfigurationLoader(self.__accessor)
        configuration_loader.load_packages()
