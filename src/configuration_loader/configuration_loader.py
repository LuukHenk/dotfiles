from pathlib import Path

from configuration_loader.parsers.package_parser import PackageParser
from data_layer.package_accessor import PackageAccessor
from logger.logger import log_error
from utils.root_finder import ROOT

class ConfigurationLoader:
    __default_config_path = ROOT / "configuration"

    def __init__(self, configuration_path: Path = __default_config_path):
        self.__packages_config_path = configuration_path / "packages.toml"

    def load_packages(self, package_accessor: PackageAccessor) -> None:
        for package in PackageParser().parse(self.__packages_config_path):
            result = package_accessor.add_package(package)
            if not result.success:
                log_error(f"Failed to load package '{package.name}': {result.message}")
