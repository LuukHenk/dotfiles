from typing import List, Dict, Union
from pathlib import Path
from src.utils.message_displayer import fail_message, success_message
from src.utils.user_validation import validate_user

OVERWRITE_MESSAGE = "{} already exists, overwrite?"
CREATE_SYMLINK_MESSAGE = "Create symlink {}?"


class DotfileSymlinking:
    def __init__(self, repository_path: Path):
        self.__repository_path: Path = repository_path

    def deploy_dotfiles(self, dotfile_paths: List[Dict[str, str]]):
        """
        Checks if the dotfiles save location already exists
        and asks the user to (re)create a symbolic link for the repo dot files

        Arguments:
            dotfiles (dict): repo path as key and deploy path as value
        """
        if not validate_user("Check if dotfiles are symlinked?"):
            return

        for dotfile_path in dotfile_paths:
            deploy_path = Path.home() / dotfile_path["deploy_path"]
            validation_message = OVERWRITE_MESSAGE if deploy_path.is_symlink() else CREATE_SYMLINK_MESSAGE
            if not validate_user(validation_message.format(deploy_path)):
                fail_message(f"Dotfile '{deploy_path}' skipped")
                continue
            self.create_symlink(dotfile_path["repository_path"], deploy_path)


    def create_symlink(self, file_name: Union[Path, str], deploy_path: Path):
        """Creates a symlink from the repo path to the deploy path"""
        deploy_path.unlink(missing_ok=True)
        deploy_path.parent.mkdir(parents=True, exist_ok=True)
        repo_path = self.__repository_path / file_name
        deploy_path.symlink_to(repo_path)
        success_message(f"Created symlink from '{repo_path}' to '{deploy_path}'")