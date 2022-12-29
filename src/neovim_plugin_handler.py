    

from pathlib import Path

from src.utils.user_validation import validate_user
from src.utils.subprocess_handler import check_exit_status_in_subprocess
from src.utils.message_displayer import fail_message, success_message
from src.dotfiles_symlinking import DotfileSymlinking
   
def install_neovim_plugins(dotfile_symlinking: DotfileSymlinking):
    """
    Neovim plugin installer - Installs Neovim plugins using the Plug script
    Plugins should be put in the init.vim file
    (https://github.com/junegunn/vim-plug)
    """
    if not validate_user("Install Neovim plugins?"):
        return

    if not check_exit_status_in_subprocess(["which", "nvim"], capture_output=True):
        fail_message("Error: Neovim not found, plugin installation skipped")
        return

    dotfile_symlinking.create_symlink(
        file_name="plug.vim",
        deploy_path=Path.home()/".config/nvim/autoload/plug.vim"
    )

    if not check_exit_status_in_subprocess(
        ["nvim", "+PlugInstall", "+PlugUpdate", "+PlugUpgrade", "+qa"],
        capture_output=True
    ):
        fail_message("Error: Failed to run the installer")
        return

    success_message("Neovim plugin installation complete")