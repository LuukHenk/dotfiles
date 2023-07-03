from typing import List, Callable

from data_models.package import Package
from package_manager_manager.package_manager_manager import PackageManagerManager


class Installer:
    def __init__(self, installation_status_callback: Callable[[int, List[str]], None]):
        self.__status_callback = installation_status_callback
        self.__package_manager_manager = PackageManagerManager()

    def install(self, packages_to_install: List[Package]):
        messages = []
        for i, package in enumerate(packages_to_install):
            success, message = self.__package_manager_manager.install_package(package)
            messages.append(message)
            percentage_done = int(i / len(packages_to_install) * 100)
            self.__status_callback(percentage_done, messages)
