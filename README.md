# My dotfiles
Version 0.1.3 <br />
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
	- Pre-installing
		- snap
		- python3
		- pip3 and pip3 yaml package

	- Basic configuration:
		- Bashrc: (manager: None, config: .bashrc, config_location: ~/.bashrc)
		- Inputrc: (manager: None, config: .inputrc, config_location: ~/.inputrc)
		- Neovim: (manager: snap, config: init.vim, config_location: ~/.config/nvim/init.vim)
		- Neovim plugins
		- xclip: (manager: apt)
		- wget: (manager: apt)

	- Standard configurarion (for work):
		- Packages form basic configuration +
		- Git: (manager: apt, config: .gitconfig, config_location: ~/.gitconfig)
		- Terminator: (manager: apt, config: terminator_config, config_location: ~/.config/terminator/config)
		- Pylint: (manager: apt)
		- Ncdu: (manager: apt/snap)
		- htop: (manager: apt/snap)
		- asdf
		- Rust (manager: asdf)
		- Python3 (manager: asdf)
		- Spotify: (manager: snap, config: ?)

	- Full configuration (for home):
		- Packages form basic configuration +
		- Nautilus: (manager: apt, config: gsettings, config_location: None)
		- Steam: (manager: apt)
		- Discord: (manager: apt/snap)
		- Firefox (manager: apt, config: ?)
		- GSettings
			- Nautilus config
			- Dock settings (bottom, icon size, autohide)
			- Clock settings
			- Favorite apps
				- Firefox Web Browser
				- Spotify
		- Dropbox: (manager: apt?, config: ?)
		- Ubuntu-drivers devices
		- Gnome extensions:
			- gir1.2-gtop-2.0 gir1.2-networkmanager-1.0  gir1.2-clutter-1.0
			- http://ubuntuhandbook.org/index.php/2019/03/display-cpu-memory-network-usage-in-ubuntu-18-04-panel/


### Changelog - v0.1.3
* Rewrite lib/config_file_installer to a class for easier usage
* Made a package version checker class (lib/package_info.py)
	1. Add packages you want to be maintained to the init function of the class
	2. Obtain packages information from package managers; currently apt and git.
	3. Let the user know if the packages are updated
	4. If the packages are not updated, show the newest version(s) available.

### To do
* T-A001: update readme

* T-B: Make one general file for the package info and its config files to install/obtain
* T-C: Add pre-installation file (python3, apt, snap and pip3 (with packages)

* T-?:
	* Add asdf package manager
	- Use Fish shell
	- Let the user install/uninstall packages

#### Bugfixes
	- Config installer did not recognise links

### Issues
