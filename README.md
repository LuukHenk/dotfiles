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

### /lib
**config_file_installer.py**: This file contains a function for the installation of configuration files in the /etc folder. The files in /etc will stay synchronized with the files in your home after the installation using the magical symlinking (so no need to run the config_file_installer.py again after altering files in the /etc folder)


### /etc
This folder contains configuration files for the terminal and neovim. They will automatically be updated when altered after the installation

* **.bashrc**: The .bashrc contains some terminal configuration
    * Aliases for programs and easy navigation
    * Terminal settings for easy navigation
    * Customised terminal coloring
    * Customised terminal prompt containing git status if availible

* **.inputrc**: The .inputrc contains some keymappings and shell configuration
    * Forward (and backward) per word using control-<arrowkeys>
    * Improved tab autocompletion

* **init.vim**: Vim config
    * (incomplete)

## Developent
### Issues
- I-A001a: .bashrc prompt overwrites current line when line is too long instead of using a newline
- I-A003: Rebuild init.vim and add readme info about init.vim
- I-A004: Automatically perform Pluginstaller for vim

### Changelog
- I-A001: Rebuild .bashrc
- I-A002: Rebuild .inputrc

### To do
- T-A001: Ask for installation of ubuntu gui config files --> Do they still work on 20.04?
- T-A002: Make a program installer
  - Use snap and apt for most of the programms and use asdf for programming languages

## References
- Thanks to [Sidney Liebrand](https://github.com/SidOfc) for helping with the basic configuration setup
- Thanks to [mathiasbynens](https://github.com/mathiasbynens/dotfiles) for some useful configuration settings


