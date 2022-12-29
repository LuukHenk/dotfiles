
from typing import List
from pathlib import Path

from src.utils.json_file_loader import load_json_file
from src.application.package_installer.package_installer_widget import PackageInstallerWidget

class PackageInstaller:
    def __init__(self, package_config_file_path: Path):
        self.__package_names = self.__load_package_config(package_config_file_path)

    def __load_package_config(self, package_config_file_path: Path) -> List[str]:
        config = load_json_file(package_config_file_path)
        return config if config else []
    @property
    def package_widget(self) -> PackageInstallerWidget:
        return PackageInstallerWidget(self.__package_names)