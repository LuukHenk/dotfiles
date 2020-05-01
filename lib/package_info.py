#/usr/bin/env python3.6

""" Obtain packages information """

### Imports {{{
#
import os
import yaml
#
#}}}

class PackagesInfo:
    """
    Obtain package information for the packages found in self.packages using the managers
    their location, found in self.managers
    """

    def __init__(self):
        self.managers_bins = {}

    def get_package_version_info(self, package, manager=None):
        """
        Get information about a package
        Returns a dict with package information
        """
        print(f"- {package}", end="\r")

        # Add or remove information needed here
        package_info = {
            "name": package,
            "installed": False,
            "manager": None,
            "version": None,
            "latest": {},
            "uptodate": False
        }

        # Determine the saving location of the package
        saving_location = os.popen("which "+package).read().split("\n")[0]

        # If the program is already installed, find the package manager and the version
        if len(saving_location) > 0:
            package_info["installed"] = True

            #try to find the package manager
            try:
                package_info["manager"] = self.managers_bins[os.path.dirname(saving_location)]
            # When there is an unknown package manager:
            except KeyError:
                print((
                    f"The '{package}' package is currently installed "
                    f"with an \x1b[31munknown package manager\x1b[39m at '{saving_location}'"
                ))
            # If there is a package manager found;
            else:

                try:
                    # Use the found package managers to obtain the package version
                    if package_info["manager"] == "snap":
                        snap_info = yaml.safe_load(os.popen(f"snap info {package}").read())
                        package_info["version"] = snap_info["installed"].split(" ")[0]

                    if package_info["manager"] == "apt":
                        apt_info = os.popen(f"apt-cache policy {package}").read().split("\n")[1]
                        package_info["version"] = apt_info.split("Installed: ")[1]
                # Can't find package version
                except:
                    print(f"Can't obtain package information for {package}...")

        # Check if there a preferred manager and find the latest version for this manager
        if manager:
            package_info["latest"] = self.get_latest_package_version(package, manager)
        else:
            versions = {}
            for _, manager_name in self.managers_bins.items():
                version = self.get_latest_package_version(package, manager_name)
                if len(version) > 0:
                    versions[manager_name] = version[manager_name]
            package_info["latest"] = versions

        # # Check if the package is up to date
        if package_info["installed"] and len(package_info["latest"]) > 0:
            latest_from_manager = package_info["latest"][package_info["manager"]]
            if package_info["version"] == latest_from_manager:
                package_info["uptodate"] = True

        return package_info

    def get_latest_package_version(self, package, manager):
        """
        Get the latest package version from all the given managers (list).
        It will use the all the managers is left as None.
        """
        latest_versions = {}

        # Get latest apt version
        if manager == "apt":
            # Perform command
            apt_info = os.popen(f"apt-cache policy {package}").read()
            if len(apt_info) > 0:
                latest_versions[manager] = apt_info.split("\n")[2].split("Candidate: ")[1]

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


    def render_version_info(self, info):
        " Let the user know if their packages are up to date "
        try:
            pack = info["name"]
            # Let the user know that the package is up to date
            if info["uptodate"]:
                print((
                    f"Package '{pack}' is up to date with the latest stable version"
                    f" of the '{info['manager']}' package manager..."
                ))

            # Let the use know that the package is installed but not up to date
            # and shows the latest stable version
            elif info["installed"]:
                print((
                    "\x1b[33m"
                    f"Warning: Package '{pack}' is not up to date with the latest stable"
                    f" '{info['manager']}' version."
                    f" Stable: v{info['latest'][info['manager']]}"
                    f"| Current: v{info['version']}"
                    "\x1b[39m"
                ))

            # Let the user know that the package is not installed
            # and show the newest versions available
            elif len(info["latest"]) > 0:
                latest_pprint = ""
                for manager, version in info["latest"].items():
                    if len(latest_pprint) > 0:
                        latest_pprint = " | ".join([latest_pprint, manager + " v" + version])
                    else:
                        latest_pprint += manager + " v" + version
                print((
                    "\x1b[33m"
                    f"Warning: Package '{pack}' is not installed yet."
                    " Latest stable versions available:"
                    f" {latest_pprint}"
                    "\x1b[39m"
                ))

            # Unable to obtain package version information
            else:
                print((
                    f"\x1b[31mCan't find information about '{pack}'...\x1b[39m"
                ))

        # Information to obtain package information is missing
        except KeyError as error:
            print((
                "\x1b[31m"
                f"Error: Failed to render '{pack}' package information ...\n"
                "The self.packages_info dictionary found in './lib/packages_installer'"
                " is missing information. (Maybe using an incorrect package manager?)"
                f"\nKeyerror: {error}"
                "\x1b[39m"
            ))
#
# }}}
