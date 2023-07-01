from pathlib import Path

from configuration_loader.parsers.package_parser import PackageParser
from old.data_layer.package_accessor import PackageAccessor


class ConfigurationLoader:
    __default_config_path = Path("../configuration")

    def __init__(self, configuration_path: Path = __default_config_path):
        self.__packages_config_path = configuration_path / "packages.toml"

    def load_packages(self, package_accessor: PackageAccessor) -> None:
        parsed_packages = PackageParser().parse(self.__packages_config_path)
