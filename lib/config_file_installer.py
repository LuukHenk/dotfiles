""" Installation of the system configuration files """

import os
import sys

def install_config_files(source_path):
    " Function to install the system configuration files"

    # Obtain files from source path
    source_files = {}
    source_files["bashrc"] = os.path.normpath(source_path+"/.bashrc")
    source_files["inputrc"] = os.path.normpath(source_path+"/.inputrc")
    source_files["nvim_config"] = os.path.normpath(source_path+"/init.vim")

    # Check if al source files exists
    for tag in source_files:
        if not os.path.isfile(source_files[tag]):
            print((
                f"\x1b[31mError: \x1b[39mSource file '{source_files[tag]}' missing. Exitting..."
                "\n(Please add the file or remove the source file from the code)"
            ))
            sys.exit()

    # Get saving paths
    home_dir = os.path.expanduser("~")
    nvim_dir = os.path.normpath("/".join([home_dir, ".config/nvim"]))

    # Map the source files to the correct saving paths
    file_map = {}
    try:
        file_map[home_dir] = [source_files["bashrc"], source_files["inputrc"]]
        file_map[nvim_dir] = [source_files["nvim_config"]]
    except KeyError as err:
        print(f"\x1b[31mError: \x1b[39mTrying to map an unknown source file: {err}...")

    # Add the source files to the correct directory
    files_saved = 0
    total_files = 0
    for directory, files in file_map.items():
        total_files += len(files)

        # Make the directory if it not exists yet
        if not os.path.isdir(directory):
            os.makedirs(directory)
            print(f"Created {directory}...")

        # Add the source file to the directory
        for file in files:
            dest = "/".join([directory, os.path.basename(file)])

            # Check destination already exists
            if os.path.isfile(dest):
                # Overwrite if the file already exitst?
                overwrite_file = input((
                    f"File '{dest}' already exists, overwrite? [y/N] "
                )).lower()
                if overwrite_file in ("y", "yes"):
                    try:
                        os.remove(dest)
                        os.symlink(file, dest)
                    except OSError:
                        print(f"\x1b[31mError: \x1b[39mFile '{dest}' can not be overwritten...")
                    else:
                        files_saved += 1
                        print(f"File '{dest}' overwritten...")

            # If the destination does not exists yet
            else:
                # Create file?
                create_file = input((
                    f"Create '{dest}'? [Y/n] "
                )).lower()
                if create_file not in ("n", "no"):
                    try:
                        os.symlink(file, dest)
                    except OSError:
                        print(f"\x1b[31mError: \x1b[39mFile '{dest}' can not be created...")
                    else:
                        files_saved += 1
                        print(f"File '{dest}' overwritten...")

    print(f"{files_saved}/{total_files} files saved")
