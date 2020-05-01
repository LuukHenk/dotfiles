#!/usr/bin/env python3.6

""" Installation of programs their configuration files """


### Imports {{{
#
import os
#
# }}}


### Config file installer {{{
#

def config_installer(config_data):
    files_saved = 0
    for source_file in config_data:
        # Generate error if the source file does not exist and skip current source file
        if not os.path.isfile(source_file):
            print((
                f"\x1b[31mError: \x1b[39mSource file '{source_file}' is missing."
            ))
            continue

        # Get the destination path and check if it already exists
        dest = config_data[source_file]
        if os.path.isfile(dest) or os.path.islink(dest):
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
                f"Create '{dest}'? [y/N] "
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

    print(f"{files_saved}/{len(config_data)} configuration files saved")
#
# }}}
