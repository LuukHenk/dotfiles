from typing import List

from logger.logger import log_error


class PackageIdTracker:
    def __init__(self):
        self.__package_ids: List[int] = []

    @property
    def package_ids(self) -> List[int]:
        return self.__package_ids

    def add_package_id(self, package_id: int) -> None:
        if package_id in self.__package_ids:
            log_error(f"Package ID {package_id} can't be added. Found a duplicate.")
            return
        self.__package_ids.append(package_id)

    def remove_package_id(self, package_id: int) -> None:
        if package_id not in self.__package_ids:
            log_error(f"Package ID {package_id} can't be removed. Not found.")
            return
        self.__package_ids.remove(package_id)
