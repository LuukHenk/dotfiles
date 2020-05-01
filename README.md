# My dotfiles
Version 0.1.4 <br />
My computer configuration setup

## References
- Thanks to [Sidney Liebrand](https://github.com/SidOfc) for helping me building these dotfiles and his vim statusbar
- Thanks to [mathiasbynens](https://github.com/mathiasbynens/dotfiles) for some useful configuration filesettings

## Installing
1. Clone the repository to your local computer: `$ git clone https://github.com/LuukHenk/dotfiles.git`
2. Run the pre-installer as sudo to install snap, python3 and python-yaml: `$ sudo sh dotfiles/pre_installer.sh`, or install snap, python3 and python-yaml yourself.
2. Make the setup installer executable: `$ chmod +x dotfiles/setup_installer`
3. Run the setup installer and follow the installation script: `$ ./setup_installer`

NOG LINKS NAAR DE JUISTE PLEK TOEVOEGEN
## The setup
### Standard packages
The packages.json file contains the information needed for the installation of packages and/or computer configuration.
The packages.json has three installation sets (basic, standard, full) of which information can be found here.
The packages.json file also keeps track of the package managers (apt, snap) and their saving destionation.





New managers / installation sets can easily be added to the packages.json file

Run the setup_installer to start the setup configuration
1. Asks for detection of package versions
2. Asks for installation of configuration files

### Package versions
(./lib/package_info.py) The versions of packages are compared with the latest stable version of the manager(s) . Programs and managers can be added to the __init__ function of the package info file.

### Configuration file installer
(./lib/config_installer.py) The configuration file installer installs configuration files found in the config source path (standard: ./etc). More files can be added to the __init__ function of the file. The configuration files will stay synchronized after the installation using the magical symlinking (so no need to run the config_file_installer.py again after altering the source files)

#### Standard configuration files (for now)
* **.bashrc**: The .bashrc contains some terminal configuration

* **.inputrc**: The .inputrc contains some keymappings and shell configuration
    * Forward (and backward) per word using control-<arrowkeys>
    * Improved tab autocompletion

* **init.vim**: Vim config
	* Plugins
	* Some alternative settings
	* Key mappings
    * Some autocommand (focusloss, trailing whitespace removal and alternative tab indenting)

### Installation sets
	- Basic configuration:
		- Bashrc
			The dotfiles/etc/.bashrc configuration file contains some shell configuration:
			* Aliases for programs and easy navigation
			* Terminal settings for easy navigation
			* Customised terminal coloring
			* Customised terminal prompt containing git status if availible

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


## Development
### Changelog - v0.1.4

### Complete package plan for release

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


### To do
	- T-A: Rewrite all commentary
	- T-B: Add all packages preferences
	- T-?:
		- Add asdf package manager
		- Add user input arguments for the PACKAGES_PREFERENCE
		- Let the user install/uninstall packages
		- Use Fish shell

### Bugfixes
	- No bugfixes yet

### Issues
	- No issues found yet
