from pathlib import Path
from typing import List

from data_models.dotfile import Dotfile
from data_models.package import Package

from data_models.item import Item
from data_models.result import Result
from installer.installing_status_widget.installation_status_widget import InstallationStatusWidget
from package_manager_manager.package_manager_manager import PackageManagerManager


class Installer:
    def __init__(self) -> None:
        self.__installation_status_widget = InstallationStatusWidget()
        self.__package_manager_manager = PackageManagerManager()
        self.__items_to_install: List[Item] = []

    @property
    def installation_status_widget(self):
        return self.__installation_status_widget

    def set_items_to_install(self, items_to_install: List[Item]):
        self.__items_to_install = items_to_install

    def install(self):
        for i, item in enumerate(self.__items_to_install):
            self.__install_item(item)
            percentage_done = int((i + 1) / len(self.__items_to_install) * 100)
            self.__installation_status_widget.update_progress_bar(percentage_done)

    def __install_item(self, item: Item):
        install_status = "Uninstalling" if item.installed else "Installing"
        self.__installation_status_widget.add_message(f"{install_status} {item.name} ...")
        if isinstance(item, Package):
            result = self.__package_manager_manager.swap_installation_status(item)
        elif isinstance(item, Dotfile):
            result = self.__swap_dotfile_symlink_status(item)
        else:
            result = Result(False, f"No installation script found for item type '{type(item)}'")
        item.installed = item.installed if not result.success else not item.installed
        self.__installation_status_widget.add_message(result.message)

    def __swap_dotfile_symlink_status(self, dotfile: Dotfile) -> Result:
        return self.__remove_dotfile_symlink(dotfile) if dotfile.installed else self.__set_dotfile_symlink(dotfile)

    @staticmethod
    def __remove_dotfile_symlink(dotfile: Dotfile) -> Result:
        try:
            dotfile.deploy_path.unlink()
        except FileNotFoundError as err:
            return Result(False, f"Unable to remove {dotfile.name}: {err}")
        return Result(True, f"Successfully removed {dotfile.name}")

    @staticmethod
    def __set_dotfile_symlink(dotfile: Dotfile) -> Result:
        if not dotfile.deploy_path.parent:
            dotfile.deploy_path.parent.mkdir(parents=True)
        dotfile.deploy_path.symlink_to(dotfile.repo_path)
        return Result(True, f"Successfully symlinked {dotfile.name} to {dotfile.deploy_path}")
