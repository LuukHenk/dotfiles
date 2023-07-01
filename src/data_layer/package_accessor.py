from typing import Optional, Dict

from data_models.version import Version

from data_models.manager_name import ManagerName
from data_models.package import Package
from data_models.result import Result
from data_models.accessor_result_message import AccessorResultMessage as ResultMessage


class PackageAccessor:
    def __init__(self):
        super().__init__()
        self.__packages: Dict[int, Package] = {}

    def find_package_via_bk(self, search_name: str, manager: ManagerName, version: Version) -> Optional[Package]:
        """Use the business keys to find the object. This will take longer then finding the object via the PK"""
        for package in self.__packages.values():
            if package.manager_name == manager and package.search_name == search_name and package.version == version:
                return package
        return None

    def find_package_via_id(self, package_id: int) -> Optional[Package]:
        """Use the primary key to find the object"""
        try:
            return self.__packages[package_id]
        except KeyError:
            return None

    def add_package(self, package: Package) -> Result:
        already_existing_package = self.find_package_via_bk(package.search_name, package.manager_name, package.version)
        if already_existing_package is not None:
            message = ResultMessage.DUPLICATION.value.format(already_existing_package.name, package.name)
            return Result(success=False, message=message)
        self.__packages[package.id_] = package
        return Result(success=True)

    def update_package(self, package_id: int, updated_package: Package) -> Result:
        package = self.find_package_via_id(package_id)
        validation_result = self.__validate_update(package, updated_package)
        if not validation_result.success:
            return validation_result

        # TODO: #0000001
        package.search_name = updated_package.search_name
        package.manager = updated_package.manager_name
        package.name = updated_package.name
        package.groups = updated_package.groups
        package.installed = updated_package.installed
        package.version = updated_package.version

    def __validate_update(self, package: Optional[Package], updated_package: Package) -> Result:
        if not package:
            return Result(success=False, message=ResultMessage.NOT_FOUND.value)
        duplicate = self.find_package_via_bk(
            updated_package.search_name, updated_package.manager_name, updated_package.version
        )
        if duplicate is not None:
            if duplicate.id_ == package.id_:
                return Result(success=False, message=ResultMessage.UNCHANGED.value)
            else:
                return Result(success=False, message=ResultMessage.DUPLICATION.value)
        return Result(success=True)
