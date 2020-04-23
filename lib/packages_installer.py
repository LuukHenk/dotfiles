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
        self.managers_bin = {
            "/usr/bin": "apt",
            "/snap/bin": "snap"
        }

        self.packages = [
            "htop", "nvim", "ncdu", "maas"
        ]

        self.package_info = [self.get_local_package_info(pack) for pack in self.packages]


    def get_local_package_info(self, package):
        """
        Get information about a package
        Returns a dict with package information
        """

        # Add or remove information needed here
        package_info = {
            "name": package,
            "version": None,
            "manager": None,
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

        return package_info
