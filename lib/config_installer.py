#!/usr/bin/env python3.6

""" Installation of the system configuration files """

FILE_PATH = "lib/config_file_installer.py"

### Imports {{{
#
import os
import sys
#
# }}}


### Config file installer {{{
#
class ConfigInstaller:
    def __init__(self):
        # Get the users home directory
        self.home = os.path.expanduser("~")

        # Set the path to the config source files
        self.config_source_path = "."

        # Set the config file and its destination
        self.config_dest = {
            ".bashrc":  self.home + "/" + ".bashrc",
            ".inputrc": self.home + "/" + ".inputrc",
            "init.vim": self.home + "/" + ".config/nvim/init.vim"
        }




    def installer(self):
        " Obtains configuration files in self.config_dest and saves them at their destination "

        # print("\033[1m Config file installer\033[0m")
        files_saved = 0

        for config_file in self.config_dest:
            # Get the full path of the config source file
            source_file = os.path.normpath(self.config_source_path+"/"+config_file)

            # Generate error if the source file does not exist and skip current source file
            if not os.path.isfile(source_file):
                print((
                    f"\x1b[31mError: \x1b[39mSource file '{source_file}' is missing."
                    f"\n(Please add the file '{source_file}' to the correct source path "
                    "or remove the source file from "
                    f"'{FILE_PATH}')"
                ))
                continue

            # Get the destination path and check if it already exists
            dest = self.config_dest[config_file]
            if os.path.isfile(dest):
                overwrite_file = input((
                    f"File '{dest}' already exists, overwrite? [y/N] "
                )).lower()

                # Overwrite the already existing config file?
                if overwrite_file in ("y", "yes"):
                    # Try to symlink config file
                    try:
                        os.remove(dest)
                        os.symlink(source_file, dest)
                    # Give error if file could not be overwritten
                    except OSError:
                        print(f"\x1b[31mError: \x1b[39mFile '{dest}' can not be overwritten...")
                    else:
                        files_saved += 1
                        print(f"File '{dest}' overwritten...")

            # If the distination path doesn't exist yet
            else:
                create_file = input((
                    f"Create '{dest}'? [y, N] "
                )).lower()

                # Generate configuration files?
                if create_file in ("y", "yes"):
                    # Try to symlink config file
                    try:
                        os.symlink(source_file, dest)
                    # Give error if file could not be overwritten
                    except OSError:
                        print(f"\x1b[31mError: \x1b[39mFile '{dest}' can not be created...")
                    else:
                        files_saved += 1
                        print(f"File '{dest}' overwritten...")

        print(f"{files_saved}/{len(self.config_dest)} configuration files saved")
#
# }}}
