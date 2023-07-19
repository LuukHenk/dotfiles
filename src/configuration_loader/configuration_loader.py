from pathlib import Path
from typing import List, Dict, Union
from tomllib import load, TOMLDecodeError

from configuration_loader.data_models.config_format import ConfigFormat
from configuration_loader.parsers.dotfile_parser import parse_dotfile_config
from configuration_loader.parsers.package_parser import PackageParser
from data_layer.dotfile_accessor import DotfileAccessor
from data_layer.package_accessor import PackageAccessor
from data_models.dotfile import Dotfile
from logger.logger import log_error, log_info
from utils.root_finder import ROOT


class ConfigurationLoader:
    __default_config_path = ROOT / "configuration" / "config.toml"

    def __init__(self, config_path: Path = __default_config_path):
        self.__config_path = config_path
        self.__config = self.__load_config(self.__config_path)
        self.__packages_config_path = ROOT / "configuration" / "packages.toml"

    def load_packages(self, package_accessor: PackageAccessor) -> None:
        packages = PackageParser().parse(self.__packages_config_path)
        log_info(f"Found {len(packages)} packages in '{self.__packages_config_path}'")
        for i, package in enumerate(packages):
            log_info(f"Loading packages: {i+1}/{len(packages)}")
            result = package_accessor.add_package(package)
            if not result.success:
                log_error(f"Failed to load package '{package.name}': {result.message}")

    def construct_dotfile_accessor(self) -> DotfileAccessor:
        accessor = DotfileAccessor()
        try:
            dotfiles = parse_dotfile_config(self.__config)
        except KeyError as key_error:
            log_error(f"Failed to parse dotfile configuration in {self.__config_path}. KeyError: {key_error}")
            return accessor

        # TODO; add dotfiles to accessor
        return accessor

    @staticmethod
    def __load_config(config_path: Path) -> ConfigFormat:
        try:
            with open(config_path, "rb") as f:
                data: ConfigFormat = load(f)
        except TOMLDecodeError as err:
            log_error(f"Failed to parse config file '{config_path}': {err}")
            raise
        return data
