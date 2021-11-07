# Dotfiles
Personalised configuration setup for Linux Ubuntu

## The setup
My personalised configuration setup script performs the following tasks:
* Check packages - Asks to check if the packages in `self.packages` are present
* Symlink dotfiles - Asks to symlink the dotfiles found in `self.dotfiles` to their deploy location
* Install Neovim plugins - Asks for installation and updating of the Neovim plugins (Using the Plug script: https://github.com/junegunn/vim-plug)
* Install Gsettings - Asks for installation of the gsettings configuration found in `etc/gsettings.json`.

## Installation
### Prerequisits
* Python3.8 or higher is needed.
* ((Python3.8 should contain the subprocess, json, pathlib and colorama packages.)) - These should be defaults

### Installation
```
$ git clone https://github.com/LuukHenk/dotfiles.git
$ chmod +x dotfiles/setup
$ ./setup
```

## References
- Thanks to [Sidney Liebrand](https://github.com/SidOfc) for helping me building these dotfiles and his vim statusbar
- Thanks to [mathiasbynens](https://github.com/mathiasbynens/dotfiles) for some useful configuration filesettings

<sub>Version 0.2.0</sub>
