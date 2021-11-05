import os
keys = os.popen("gsettings list-keys org.gnome.desktop.wm.keybindings").read().split("\n")[:-1]

command = "gsettings get org.gnome.desktop.wm.keybindings "
for key in keys:
    out = os.popen(command + key).read()
    if "<Super>h" in out:
        print("\n" + key)
        print(out)
