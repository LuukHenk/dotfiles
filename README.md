# My dotfiles
Version 0.1.1 <br />
My computer configuration setup

## Installing
1. Clone the repository to your local computer: `$ git clone https://github.com/LuukHenk/dotfiles.git`
2. Make the setup installer executable: `$ chmod +x dotfiles/setup_installer`
3. Run the setup installer and follow the installation script: `$ ./setup_installer`

## The setup
### setup_installer
Run this file to start the setup installation

### lib/
#### config_file_installer.py
This file contains a function for the installation of configuration files in the etc/ folder. The configuration will automatically be updated when altering these files using the magical symlinking (no need to run the config_file_installer.py after altering files etc/)


### etc/
This folder contains configuration files for the terminal and neovim. They will automatically be updated when altered after the installation

#### .bashrc
The .bashrc contains some shell configuration
- Case insensitivity
- Append history rather than overwrite it
- Autocorrection
- Auto cd
- Tab completion
- Costumised terminal coloring
- Added some aliases

#### .inputrc
The .inputrc contains some keymappings and shell configuration
- Added forwarding per word
- Tweaked the Tab autocompletion

#### input.vim
Vim config

## Developent
### Issues
- Add ubuntu configuration files
- Make a program installer
- Add nvim plugin installer


### Changelog

#### To do
## References
- Thanks to [Sidney Liebrand](https://github.com/SidOfc) for helping with the basic configuration setup
- Thanks to [mathiasbynens](https://github.com/mathiasbynens/dotfiles) for some useful configuration settings


