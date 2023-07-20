from pathlib import Path
from typing import List
from tomllib import load, TOMLDecodeError


from configuration_loader.data_models.config_format import ConfigFormat
from configuration_loader.parsers.dotfile_parser import parse_dotfile_config
from configuration_loader.parsers.package_parser import PackageParser

from data_models.item import Item
from logger.logger import log_error
from utils.root_finder import ROOT


class ConfigurationLoader:
    __default_config_path = ROOT / "configuration" / "config.toml"

    def __init__(self, config_path: Path = __default_config_path):
        self.__config_path = config_path
        self.__config = self.__load_config_from_toml_file(self.__config_path)

    def load_config(self) -> List[Item]:
        items = []
        try:
            items += parse_dotfile_config(self.__config)
            items += PackageParser().parse_packages_config(self.__config)
        except KeyError as key_error:
            log_error(f"Failed to parse configuration in {self.__config_path}. KeyError: {key_error}")
            return items
        return items

    @staticmethod
    def __load_config_from_toml_file(config_path: Path) -> ConfigFormat:
        try:
            with open(config_path, "rb") as f:
                data: ConfigFormat = load(f)
        except TOMLDecodeError as err:
            log_error(f"Failed to parse config file '{config_path}': {err}")
            raise
        return data
