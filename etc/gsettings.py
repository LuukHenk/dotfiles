DATA = {
    ### Dock settings
    "org.gnome.shell.extensions.dash-to-dock": {
        # Dock position
        "dock-position": "BOTTOM",
        # Dock icon size
        "dash-max-icon-size": "16",
        # Dock autohide
        "autohide": "true",
        "dock-fixed": "false",
        "intellihide": "true"
    },
    ### Favorite apps in dock
    "org.gnome.shell": {
        "favorite-apps": "\"['firefox.desktop', 'spotify_spotify.desktop']\""
    },
    ### Desktop interface
    "org.gnome.desktop.interface": {
        # Clock show date/seconds/weekday
        "clock-show-date": "true",
        "clock-show-seconds": "true",
        "clock-show-weekday": "true",
        # Show battery percentage
        "show-battery-percentage": "true",
        "gtk-theme": "\"'Yaru-dark'\"",
        "icon-theme": "\"'Yaru'\""
    },
    ### Desktop icons
    "org.gnome.shell.extensions.desktop-icons": {
        "show-trash": "false",
        "show-home": "false"
    },
    ### Ibus emoij keybindings
    "org.freedesktop.ibus.panel.emoji": {
        # Remove emoij hotkey, as it interferes with the terminator hotkeys
        "hotkey": "\"['']\""
    },
    ### Input sources
    "org.gnome.desktop.input-sources" : {
        # Use casp-lock as an escape key
        "xkb-options": "\"['caps:escape']\""
    },
    ### Keybinds
    "org.gnome.desktop.wm.keybindings": {
        "close": "\"['<Control><Alt>w']\"",
        "unmaximize": "\"['<Alt>F5']\"",
        "minimize": "\"['<Super>Down']\""
    },
    ### Colors
    "org.gnome.settings-daemon.plugins.color": {
        # Set nightlight settings
        "night-light-schedule-automatic": "true",
        "night-light-enabled": "true",
        "night-light-temperature": "3000"
    },
    ### Privacy
    "org.gnome.desktop.privacy": {
        # Remember file history
        "remember-recent-files": "true",
        "recent-files-max-age": "30",
        # Keep temporarly/trash files
        "remove-old-temp-files": "true",
        "remove-old-trash-files": "true",
        "old-files-age": "30",
        # Disable camera
        "disable-camera": "true"
    }
}

