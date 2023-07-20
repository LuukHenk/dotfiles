from pathlib import Path
from typing import List


from configuration_loader.data_models.config_format import ConfigFormat
from configuration_loader.data_models.config_keys import ConfigKeys
from data_models.dotfile import Dotfile


def parse_dotfile_config(config: ConfigFormat) -> List[Dotfile]:
    dotfiles = []
    for dotfile_config in config[ConfigKeys.DOTFILES]:
        deploy_path = Path(dotfile_config[ConfigKeys.DEPLOY_PATH]).expanduser()
        repo_path = Path(dotfile_config[ConfigKeys.REPO_PATH]).expanduser()
        dotfile = Dotfile(
            repo_path=repo_path,
            deploy_path=deploy_path,
            installed=deploy_path.is_file(),
            name=dotfile_config[ConfigKeys.NAME],
            group=dotfile_config[ConfigKeys.GROUP],
            installation_request=False,
        )
        dotfiles.append(dotfile)
    return dotfiles
