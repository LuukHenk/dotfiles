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
    " Install configuration files found in 'config_data': {source_path: dest_path}, ..."

    files_saved = 0
    # Loop over all paths in config_data
    for source_path in config_data:

        # Generate error if the source file does not exist and skip current source file
        if not os.path.isfile(source_path):
            print((
                f"\x1b[31mError: \x1b[39mSource file '{source_path}' is missing."
            ))
            continue

        # Get the destination path and check if it already exists
        dest_path = config_data[source_path]
        if os.path.isfile(dest_path) or os.path.islink(dest_path):
            overwrite_file = input((
                f"File '{dest_path}' already exists, overwrite? [y/N] "
            )).lower()

            # Overwrite the already existing config file?
            if overwrite_file in ("y", "yes"):
                # Try to symlink config file
                try:
                    os.remove(dest_path)
                    os.symlink(source_path, dest_path)
                # Give error if file could not be overwritten
                except OSError:
                    print((
                        "\x1b[31mError: \x1b[39m"
                        f"File '{dest_path}' can not be overwritten..."
                    ))
                else:
                    files_saved += 1
                    print(f"File '{dest_path}' overwritten...")

        # If the distination path doesn't exist yet
        else:
            create_file = input((
                f"Create '{dest_path}'? [y/N] "
            )).lower()

            # Generate configuration files?
            if create_file in ("y", "yes"):
                # Try to symlink config file
                try:
                    dest_dir = os.path.dirname(dest_path)
                    if not os.path.isdir(dest_path):
                        os.makedirs(dest_dir)
                    os.symlink(source_path, dest_path)
                # Give error if file could not be overwritten
                except OSError:
                    print(f"\x1b[31mError: \x1b[39mFile '{dest_path}' can not be created...")
                    os.symlink(source_path, dest_path)
                else:
                    files_saved += 1
                    print(f"File '{dest_path}' written...")

    print(f"{files_saved}/{len(config_data)} configuration files saved")
#
# }}}
