# My dotfiles
Version 0.1.5 <br />
My computer configuration setup

## References
- Thanks to [Sidney Liebrand](https://github.com/SidOfc) for helping me building these dotfiles and his vim statusbar
- Thanks to [mathiasbynens](https://github.com/mathiasbynens/dotfiles) for some useful configuration filesettings

## Installing
1. Clone the repository to your local computer: `$ git clone https://github.com/LuukHenk/dotfiles.git`
2. Run the pre-installer as sudo to install snap, python3 and python-yaml: `$ sudo sh dotfiles/pre_installer.sh`, or install snap, python3 and python-yaml by yourself.
2. Make the setup installer executable: `$ chmod +x dotfiles/setup_installer`
3. Run the setup installer and follow the installation script: `$ ./setup_installer`

## The setup

### Pre-set package managers
The pre-set package managers and their package destination (bin folder) can be found in the packages.json file in the 'packages_bin' dictionary.

### Pre-set configuration sets
All configuration sets can be found in the packages.json file below the mangers_bins dictionary

**Basic configuration set ("basic")**
- bashrc:
	Symlink configuration file './etc/bashrc' to '~/.bashrc'

        Contains:
		- Aliases for programs
		- Easy navigation in shell
		- Customised terminal coloring
		- Customised terminal prompt, containing git status if availible

- inputrc:
	Symlink configuration file './etc/inputrc' to '~/.inputrc'

        Contains:
		- Forward (and backward) line per word in the shell using control-<arrowkeys>
		- Improved shell tab autocompletion

- xclip:
	Check for the 'xclip' version using the 'apt' package manager

- wget
	Check for the 'wget' version using the 'apt' package manager

 - Neovim (Plugin manager file is owned by [Junegunn](Junegunn/vim-plug))

	Check for the 'nvim' version using the 'snap' package manager

	Symlink configuration file './etc/init.vim' to '~/.config/nvim/init.vim'

        Contains:
		- Neovim plugins
		- Some alternative neovim settings
		- Neovim key mappings
		- Some neovim autocommand (focusloss, trailing whitespace removal and alternative tab indenting)

	Symlink the nvim plugin manager file './etc/plug.vim' to '~/.config/nvim/autoload/plug.vim' and install, update and upgrade the plugins.

**Standard configuration**
Will be added later....

**Full configuration**
Will be added later....


### Adding new configuration packages/sets/managers
Will be added later....

## Development
### Changelog - v0.1.5

### To do
	- T1: add user settings
	- T2: update terminator config file

	- T-A: Add standard and full configuration set
	- T-B: Update README:
		- update pre-set package managers information

	- T-?:
		- Add asdf package manager
		- Add user input arguments for the PACKAGES_PREFERENCE
		- Let the user install/uninstall packages
		- Use Fish shell

### Bugfixes
	- No bugfixes yet

### Issues
	-001 Too many branches in setup_installer main function

### Complete package plan for release

	- Pre-installing
		- snap
		- python3
		- python3-yaml package

	- Basic configuration:
		- Bashrc: (manager: None, config: .bashrc, config_location: ~/.bashrc)
		- Inputrc: (manager: None, config: .inputrc, config_location: ~/.inputrc)
		- Neovim: (manager: snap, config: init.vim, config_location: ~/.config/nvim/init.vim)
		- Neovim plugins
		- xclip: (manager: apt)
		- wget: (manager: apt)
		- python3-pip
		- pip3 pylint

	- Standard configurarion (for work):
		- Packages form basic configuration +
		- Firefox (manager: apt, config: ?)
		- Git: (manager: apt, config: .gitconfig, config_location: ~/.gitconfig)
		- Terminator: (manager: apt, config: terminator_config, config_location: ~/.config/terminator/config)
		- Pylint: (manager: apt)
		- Ncdu: (manager: apt/snap)
		- htop: (manager: apt/snap)
		- asdf
		- Rust (manager: asdf)
		- Python3 (manager: asdf)
		- Spotify: (manager: snap, config: ?)
		- Nautilus: (manager: apt, config: gsettings, config_location: None)
		- GSettings
			- Nautilus config
			- Dock settings (bottom, icon size, autohide)
			- Clock settings
			- Use casp key as escape
			- Favorite apps
				- Firefox Web Browser
				- Spotify

	- Full configuration (for home):
		- Packages form basic configuration +
		- Steam: (manager: apt)
		- Discord: (manager: apt/snap)
		- Dropbox: (manager: apt?, config: ?)
		- Ubuntu-drivers devices
		- Gnome extensions:
			- gir1.2-gtop-2.0 gir1.2-networkmanager-1.0  gir1.2-clutter-1.0
			- http://ubuntuhandbook.org/index.php/2019/03/display-cpu-memory-network-usage-in-ubuntu-18-04-panel/
