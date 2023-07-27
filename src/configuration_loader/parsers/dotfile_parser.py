from os import getlogin
from pathlib import Path
from typing import List

from logger.logger import log_error

from configuration_loader.data_models.config_format import ConfigFormat
from configuration_loader.data_models.config_keys import ConfigKeys
from data_models.dotfile import Dotfile


def parse_dotfile_config(config: ConfigFormat, repo_folder: Path) -> List[Dotfile]:
    dotfiles = []
    for dotfile_config in config[ConfigKeys.DOTFILES]:
        deploy_path = __format_deploy_path(dotfile_config[ConfigKeys.DEPLOY_PATH])
        repo_path = (
            repo_folder / Path(dotfile_config[ConfigKeys.REPO_PATH]).expanduser()
        )
        if not repo_path.exists():
            log_error(
                f"Dotfile not found in the configuration folder: {dotfile_config[ConfigKeys.NAME]}"
            )
        dotfile = Dotfile(
            repo_path=repo_path,
            deploy_path=deploy_path,
            installed=deploy_path.is_file(),
            name=dotfile_config[ConfigKeys.NAME],
            group=dotfile_config[ConfigKeys.GROUP],
        )
        dotfiles.append(dotfile)
    return dotfiles


def __format_deploy_path(deploy_path_str: str) -> Path:
    if deploy_path_str and deploy_path_str[0] == "~":
        return Path(f"/home/{getlogin()}{deploy_path_str[1:]}")
    return Path(deploy_path_str).expanduser()
