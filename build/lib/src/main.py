#!/usr/bin/env python3

from .user_validation import validate
import subprocess
import json
from pathlib import Path
from colorama import Fore, Style

class Dotfiles:
    """
    Class containing configuration scripts for a linux ubuntu computer:
    1. Package checker - Checks if packages are installed.
        Packages to be checked can be put in self.packages below
    2. Dotfile symlinker - Symlinks dotfile configuration files
        from the current repo to their deploy path
        Dotfiles to be symlinked can be put in self.dotfiles below.
    3. Neovim plugin installer - Installs Neovim plugins using the Plug script
        Plugins should be put in the init.vim file
        (https://github.com/junegunn/vim-plug)
    4. Gsettings config installer - Installs the gsettings configuration
        Settings can be found in the gsettings.json script in the repo path

    The above configuration script can all be executed using the
        install() function
    """

    def __init__(self):
        repo = Path().absolute()/"etc"
        self.packages = [
            "nvim",
            "terminator",
            "wget",
            "python3",
            "pip3",
            "htop",
            "pylint",
            "git",
	    "ncdu",
            "gnome-tweaks"
        ]
        self.dotfiles = {
            # Repo_path          Deploy_path
            repo/"bashrc":       Path.home()/".bashrc",
            repo/"inputrc":      Path.home()/".inputrc",
            repo/"terminator":   Path.home()/".config/terminator/config",
            repo/"init.vim":     Path.home()/".config/nvim/init.vim",
        }
        self.nvim_plug_path = {
            "repo_path": repo/"plug.vim",
            "deploy_path": Path.home()/".config/nvim/autoload/plug.vim"
        }
        self.gsettings_config_path = repo/"gsettings.json"

    def install(self):
        """ Run the installation functions """
        self.check_packages()
        self.symlink_dotfiles()
        self.neovim_plugin_installer()
        self.gsetting_config_installer()

    def check_packages(self):
        """
        Checks if the given packages are installed by checking the
        save location

        Arguments:
            packages (list): list of package names
        """

        if not validate("Check if apt packages are installed?"):
            return

        for package in self.packages:
            try:
                subprocess.run(
                    ["which", package], check=True, capture_output=True
                )
                print(f"{Fore.GREEN}Package {package} is installed")
            except subprocess.CalledProcessError:
                print(f"{Fore.RED}Package {package} is not installed")
        print(Style.RESET_ALL)


    def symlink_dotfiles(self):
        """
        Checks if the dotfiles save location already exists
        and asks the user to (re)create a symbolic link for the repo dot files

        Arguments:
            dotfiles (dict): repo path as key and deploy path as value
        """
        answer = input(f"-- Check if dotfiles are symlinked? [y/N]")
        if answer.lower() not in ["y", "yes"]:
            return

        for repo_path, deploy_path in self.dotfiles.items():
            if deploy_path.is_symlink():
                answer = input(f"{deploy_path} already exists, overwrite? [y/N]")
            else:
                answer = input(f"Create symlink {deploy_path}? [y/N]")

            if answer.lower() in ["y", "yes"]:
                deploy_path.unlink(missing_ok=True)
                deploy_path.parent.mkdir(parents=True, exist_ok=True)
                deploy_path.symlink_to(repo_path)
                print(f"Created symlink from {repo_path} to {deploy_path}")

    def neovim_plugin_installer(self):
        """
        Checks if neovim is installed. The function is skipped if not installed
        Then deploys the pluginstaller packages
        Finally tries to install the plugins

        Arguments:
            plug (dict): should contain
                'deploy_path': <deploy location> and
                'repo_path': <plug file in repo>
        """
        answer = input("-- Install Neovim plugins? [y/N]")
        if answer.lower() not in ["y", "yes"]:
            return

        try:
            subprocess.run(["which", "nvim"], check=True, capture_output=True)
        except subprocess.CalledProcessError:
            print("".join([
                f"{Fore.RED}Error{Style.RESET_ALL}: Neovim not found, ",
                "plugin installation skipped"
            ]))
            return

        # Deploy pluginstaller
        self.nvim_plug_path["deploy_path"].unlink(missing_ok=True)
        self.nvim_plug_path["deploy_path"].parent.mkdir(parents=True, exist_ok=True)
        self.nvim_plug_path["deploy_path"].symlink_to(
            self.nvim_plug_path["repo_path"]
        )

        try:
            subprocess.run(
                ["nvim", "+PlugInstall", "+PlugUpdate", "+PlugUpgrade", "+qa"],
                check=True
            )
        except subprocess.CalledProcessError as error:
            print("".join([
                f"{Fore.RED}Error{Style.RESET_ALL}: Failed to run the installer.",
                f"{error}"
            ]))
            return
        print("Neovim plugin installation complete")

    def gsetting_config_installer(self):
        """
        Installs the configuration for the gsettings, which should be located
        in the gsetting_config_path json file.

        arguments:
            gsetting_config_path: Path to the JSON gsetting configuration file
        """

        answer = input("-- Install gsettings configuration? [y/N]")
        if answer.lower() not in ["y", "yes"]:
            return

        try:
            gconfig = json.load(open(self.gsettings_config_path, "r"))
        except FileNotFoundError:
            print("".join([
                f"{Fore.RED}Error{Style.RESET_ALL}: ",
                "gsettings config file not found. ",
                "Skippig gsettings configuration installation."
            ]))
            return

        for schema in gconfig:
            for key, value in gconfig[schema].items():
                setting = ["gsettings", "set", schema, key, value]
                setting_str = " ".join(setting)
                try:
                    subprocess.run(setting, check=True)
                    print(f"Processing '{setting_str}'")
                except subprocess.CalledProcessError:
                    print("".join([
                        f"Invalid config setting skipped: '{setting_str}'",
                        ""
                    ]))

if __name__ == "__main__":
    DOTFILES = Dotfiles()
    DOTFILES.install()