#!/usr/bin/env python3.6

""" Install desired packages """

### Imports {{{
#
import os
import yaml
#
#}}}
class Installer:
    def __init__(self):

        # Add or remove packages here (and the preferred managers (list), set none if there is no preference)
        #TODO make dict with preferred manager as value
        self.packages = {
            # "asdf": None,
            # "snap": None,
            "git": None,
            "htop": None,
            "ncdu": None,
            "nvim": None,
            "terminator": None,
            "xclip": ["apt"]
        }

        # Add or remove managers and their location here
        self.managers = {
            "apt": "/usr/bin",
            "snap": "/snap/bin"
        }
        self.managers_bin = {v: k for (k, v) in self.managers.items()}

        ##########

        # Get information about all packages
        self.packages_info = {p: self.get_package_info(p) for p in self.packages}

        for pack, info in self.packages_info.items():
            print(f"\n{pack}\n{info}")
                # else:

                #     # If the package is on the latest version
                #     if pack_info["version"] == pack_info["latest"]:
                #         print((
                #             f"'{pack}' is up to date with the "
                #             f"'{pack_info['manager']}' package manager..."
                #         ))

                #     # If the package is not on the latest version
                #     else:
                #         print((
                #             f"\x1b[33mPackage '{pack}' is not up to date with the latest stable "
                #             f"'{pack_info['manager']}' version. "
                #             f"Current version: v{pack_info['version']}\x1b[39m"
                #         ))

            # # If the package is not installed yet
            # else:
                # print((
                #     f"\x1b[31mPackage '{pack}' is not installed yet...\x1b[39m"
                # ))


    def get_package_info(self, package):
        """
        Get information about a package
        Returns a dict with package information
        """
        print(f"Searching for '{package}' package information...")

        # Add or remove information needed here
        package_info = {
            "name": package,
            "installed": False,
            "version": None,
            "manager": None,
            "latest": "",
            "uptodate": False
        }

        # Determine the saving location of the package
        # print("\nSearching for " + package + " ...")
        saving_location = os.popen("which "+package).read().split("\n")[0]
        if len(saving_location) > 0:

            #try to find the package manager
            try:
                package_manager = self.managers_bin[os.path.dirname(saving_location)]
                package_info["manager"] = package_manager

            # When there is an unknown package manager:
            except KeyError:
                print((
                    f"The '{package}' package is currently installed "
                    f"with an \x1b[31munknown package manager\x1b[39m at '{saving_location}'"
                ))

            # If there is a package manager found;
            else:
                # Use the found package managers to obtain info about the package
                try:

                    if package_manager == "snap":
                        snap_info = yaml.safe_load(os.popen(f"snap info {package}").read())
                        package_info["version"] = snap_info["installed"].split(" ")[0]

                    if package_manager == "apt":
                        apt_info = yaml.safe_load(os.popen(f"apt-cache show {package}").read())
                        package_info["version"] = apt_info["Version"]

                # Can't find package version
                except:
                    print(f"Can't obtain package information for {package}...")

        # Check if the package is installed
        package_info["installed"] = any([
            bool(package_info["version"]),
            bool(package_info["manager"])
        ])

        # Check if there a preferred manager and find the latest version for this manager
        preferred_managers = self.packages[package]
        package_info["latest"] = self.managers_latest_versions(package, preferred_managers)

        # Check if the package is up to date
        if package_info["installed"]:
            latest_from_manager = package_info["latest"][package_info["manager"]]
            if package_info["version"] == latest_from_manager:
                package_info["uptodate"] = True

        return package_info

    def managers_latest_versions(self, package, managers=None):
        latest_versions = {}

        managers = self.managers if not managers else managers
        for manager in managers:

            # Get latest apt version
            if manager == "apt":
                # Perform command
                packages_found = os.popen("apt-cache madison "+package).read().split("\n")
                for pack in packages_found:
                    # If the package is found
                    if pack.split(" | ")[0].strip() == package:
                        latest_versions[manager] = pack.split(" | ")[1].strip()

            # Get latest snap version
            if manager == "snap":
                # Perform command
                packages_found = os.popen("snap find "+package).read().split("\n")[1:]

                # Find the version of the package
                for pack in packages_found:
                    package_info = list(filter(None, pack.split(" ")))
                    if len(package_info) > 0 and package_info[0] == package:
                        latest_versions[manager] = package_info[1]

        return latest_versions




