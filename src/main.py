#!/usr/bin/env python3

from typing import Union, List, Optional
from json import loads
from pathlib import Path

from src.gsettings import GSETTINGS_CONFIG_FORMAT, set_gsettings
from src.utils.message_displayer import fail_message
from src.packages_validator import display_installed_packages
from src.dotfiles_symlinking import DotfileSymlinking
from src.neovim_plugin_handler import install_neovim_plugins


class Dotfiles:
    """
    Class containing configuration scripts for a linux ubuntu computer:
    The configuration script can all be executed using the
        install() function
    """

    def __init__(self):
        self.__repository_path = Path().absolute()/"etc"
        self.__dotfile_symlinking = DotfileSymlinking(self.__repository_path)

    def install(self):
        """ Run the installation functions """
        self.__display_installed_packages()
        self.__deploy_dotfiles()        
        install_neovim_plugins(self.__dotfile_symlinking)
        self.__set_gsettings()

    def __display_installed_packages(self):
        packages: Optional[List[str]] = self.__load_json_file("packages.json")
        if packages:
            display_installed_packages(packages)

    def __deploy_dotfiles(self):
        dotfile_paths = self.__load_json_file("dotfile_paths.json")
        if dotfile_paths:
            self.__dotfile_symlinking.deploy_dotfiles(dotfile_paths)

    def __set_gsettings(self):
        gsettings_config: GSETTINGS_CONFIG_FORMAT = self.__load_json_file("gsettings.json")
        if gsettings_config:
            set_gsettings(gsettings_config)

    def __load_json_file(self, filename: Union[str, Path]) -> any:
        """Loads a json file from the default repo path"""
        try:
            with open(self.__repository_path/filename, "r") as json_file:
                json_data = json_file.read()
            return loads(json_data)
        except FileNotFoundError as err:
            fail_message(err)
            return

if __name__ == "__main__":
    DOTFILES = Dotfiles()
    DOTFILES.install()
