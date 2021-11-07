# My dotfiles
Version 0.2.0 <br />
My computer configuration setup

## References
- Thanks to [Sidney Liebrand](https://github.com/SidOfc) for helping me building these dotfiles and his vim statusbar
- Thanks to [mathiasbynens](https://github.com/mathiasbynens/dotfiles) for some useful configuration filesettings

## Setup
### Prerequisits
Python3.8 or higher is needed.
Python3.8 should contain the subprocess, json, pathlib and colorama packages.

### Installation
1. Clone the repository to your local computer: `$ git clone https://github.com/LuukHenk/dotfiles.git`
2. Make the setup installer executable: `$ chmod +x dotfiles/setup`
3. Run the setup installer and follow the installation script: `$ ./setup`


## The setup script
The setup script performs the following tasks:
* Package checker - Asks to check if the packages in `self.packages` are present
* Dotfile symlinker - Asks to symlink the dotfiles found in `self.dotfiles` to their deploy location
* Neovim plugin installer - Asks for installation and updating of the Neovim plugins (Using the Plug script: https://github.com/junegunn/vim-plug)
* Gsettings config installer - Installs the gsettings configuration found in `etc/gsettings.json`.

## Defaults dotfile settings
### Bashrc
- Easy navigation in shell
- Customised terminal coloring
- Customised terminal prompt, containing git status if availible

### Inputrc
- Forward (and backward) line per word in the shell using control-<arrowkeys>
- Improved shell tab autocompletion

### Neovim init file
- Neovim plugins
- Some alternative neovim settings
- Neovim key mappings
- Some neovim autocommand (focusloss, trailing whitespace removal and alternative tab indenting)
