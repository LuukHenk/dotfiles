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

Complete package plan:
	- Config files (found in /etc) - standard
		- bashrc - v
		- inputrc - v
		- init.vim - v
		- git
		- terminator
		- nautilus


	- apt (& snap) - standard
		- snapd - need berfore python script
		- asdf - need before python script
		- pip3 - need before python script
		- git
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
		- Update package managers
		- Default computer settings
			- gsettings
				- hotkeys
			- default apps (can I do this with gsettings?)
				- web: Firefox Web Browser
				- Text editor: ?

### Changelog - v0.1.3
* Rewrite lib/config_file_installer to a class for easier usage
* Made a package version checker class (lib/package_info.py)
	1. Add packages you want to be maintained to the init function of the class
	2. Obtain packages information from package managers; currently apt and git.
	3. Let the user know if the packages are updated
	4. If the packages are not updated, show the newest version(s) available.

### To do
* T-B001: Add asdf package manager to program info
* T-B002: update readme about lib/package_info
* T-B003: Check all files for correct commenting
- T-B003: Check readme

- T-C: Make one general file for the package info and its config files to install/obtain
- T-D: Add pre-installation file (python3, apt, snap and pip3 (with packages)
* T-E: Let the user install/uninstall packages

#### Bugfixes

### Issues
