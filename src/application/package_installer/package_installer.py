
from typing import List
from pathlib import Path

from src.utils.json_file_loader import load_json_file
from src.application.package_installer.package import Package
from src.application.package_installer.package_installer_widget import PackageInstallerWidget
from src.utils.subprocess_handler import check_exit_status_in_subprocess

class PackageInstaller:
    def __init__(self, package_config_file_path: Path):
        self.__packages = self.__load_packages(package_config_file_path)
        self.__package_installer_widget = PackageInstallerWidget(self.__packages)

    @property
    def package_widget(self) -> PackageInstallerWidget:
        return self.__package_installer_widget

    def get_installation_commands(self) -> List[str]:
        """Get the installation commands for the selected packages"""
        commands = []
        packages_to_install = self.__package_installer_widget.get_checked_packages()
        for package_name in packages_to_install:
            commands.append(f"sudo apt install {package_name} -y")
        return commands

    def __load_packages(self, package_config_file_path: Path) -> List[Package]:
        packages = []
        package_names = load_json_file(package_config_file_path)
        package_names = package_names if package_names else []
        for package_name in package_names:
            package = Package(
                name=package_name,
                installed=self.__validate_if_package_is_installed(package_name),
            )
            packages.append(package)
        return packages

    @staticmethod
    def __validate_if_package_is_installed(package_name: str) -> bool:
        """Validates if the package exists"""
        return check_exit_status_in_subprocess(["which", package_name], capture_output=True)

