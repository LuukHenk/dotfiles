from pathlib import Path

from configuration_loader.parsers.package_parser import PackageParser
from data_layer.accessor import Accessor


class ConfigurationLoader:
    __default_config_path = Path("configuration")
    __PACKAGES_CONFIGURATION_FILE_NAME = "packages.toml"

    def __init__(self, accessor: Accessor, configuration_path: Path = __default_config_path):
        self.__accessor = accessor
        self.__configuration_path = configuration_path

    def load_packages(self) -> None:
        PackageParser().parse_toml_file(self.__configuration_path / self.__PACKAGES_CONFIGURATION_FILE_NAME)
