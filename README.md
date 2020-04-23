# My dotfiles
Version 0.1.2 <br />
My computer configuration setup

## References
- Thanks to [Sidney Liebrand](https://github.com/SidOfc) for helping me building these dotfiles and his vim statusbar
- Thanks to [mathiasbynens](https://github.com/mathiasbynens/dotfiles) for some useful configuration filesettings

## Installing
1. Clone the repository to your local computer: `$ git clone https://github.com/LuukHenk/dotfiles.git`
2. Make the setup installer executable: `$ chmod +x dotfiles/setup_installer`
3. Run the setup installer and follow the installation script: `$ ./setup_installer`

## The file setup
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
	* Plugins
	* Some alternative settings
	* Key mappings
    * Some autocommand (focusloss, trailing whitespace removal and alternative tab indenting)

## Development

### Changelog - v0.1.3

### To do
* T-A001: Rewrite lib/config_file_installer to a class
* T-B001: Check where packages are currently installed on the system (and get info) using snap and apt
* T-B001a: Add asdf package manager to program installer test
* T-B002: Check if there are newer versions of the packages availible than the one currently installed and determine if it is installed with the preferred package manager
* T-B003: Let the user install packages (??and remove the other versions after installation??)
* T-B004: Let the user uninstall packages
* T-B004: Add packages:
	- Config files (found in /etc) - standard
		- bashrc - v
		- inputrc - v
		- init.vim
		- git
		- terminator
		- nautilus


	- apt (& snap) - standard
		- snapd
		- git
		- asdf
		- pip3
		- xclip
		- ncdu
		- neovim
		- htop
		- gsettings
		- terminator

	- ASDF - Programming languages - standard
		- Rust
		- Python3
		- Bash

	- apt & snap - only for home computer
		- spotify
		- dropbox
		- steam
		- discord
		- firefox
		- nautilus (file manager) (set as default file manager)
		- nvidea driver (if available)

	- Other - ?? yet
		- Neovim plugins
		- Default computer settings
			- gsettings
				- hotkeys
			- default apps (can I do this with gsettings?)
				- web: Firefox Web Browser
				- Text editor:

- T-C: Ask for installation of ubuntu gui config files --> Do they still work on 20.04?

#### Bugfixes

### Issues
	- I-B001a: python3, pip3 and pip3 yank must be installed before we can use it



