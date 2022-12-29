
from typing import List, Optional
from pathlib import Path
from src.application.dotfile_deployer.dotfile_deployer_widget import DotfileDeployerWidget
from src.application.dotfile_deployer.dotfile import Dotfile
from src.utils.json_file_loader import load_json_file


OVERWRITE_MESSAGE = "Dotfile {} already exists, overwrite?"

class DotfileDeployer:
    def __init__(self, dotfiles_config_file_path: Path, dotfile_directory: Path):
        self.__dotfiles = self.__load_dotfiles(dotfiles_config_file_path, dotfile_directory)
        self.__dotfile_deployer_widget = DotfileDeployerWidget(self.__dotfiles)

    @property
    def dotfile_deployer_widget(self) -> DotfileDeployerWidget:
        return self.__dotfile_deployer_widget

    def deploy_dotfiles(self) -> None:
        for dotfile_name in self.__dotfile_deployer_widget.get_checked_dotfiles():
            dotfile = self.__find_dotfile_via_name(dotfile_name)
            if dotfile.deploy_path.is_symlink():
                overwrite = self.__dotfile_deployer_widget.overwrite_dialog(
                    OVERWRITE_MESSAGE.format(dotfile.deploy_path)
                )
                if not overwrite:
                    continue
            self.__create_symlink(dotfile)

    def __find_dotfile_via_name(self, dotfile_name: str) -> Optional[Dotfile]:
        """Returns the first dotfile that matches the name"""
        for dotfile in self.__dotfiles:
            if dotfile.name == dotfile_name:
                return dotfile

    @staticmethod
    def __create_symlink(dotfile:Dotfile):
        """Creates a symlink from the repo path to the deploy path"""
        dotfile.deploy_path.unlink(missing_ok=True)
        dotfile.deploy_path.parent.mkdir(parents=True, exist_ok=True)
        dotfile.deploy_path.symlink_to(dotfile.repository_path)

    def __load_dotfiles(
        self, dotfile_config_file_path: Path, dotfile_directory: Path
    ) -> List[Dotfile]:
        dotfiles = []
        dotfiles_config = load_json_file(dotfile_config_file_path)
        dotfiles_config = dotfiles_config if dotfiles_config else []
        deploy_directory = Path.home()
        for dotfile_config in dotfiles_config:
            dotfile = Dotfile(
                name=dotfile_config["repository_path"],
                repository_path=dotfile_directory/dotfile_config["repository_path"],
                deploy_path=deploy_directory/dotfile_config["deploy_path"]
            )
            dotfiles.append(dotfile)
        return dotfiles