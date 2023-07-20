from abc import ABC, abstractmethod
from typing import List

from data_models.package_old import PackageOld
from data_models.package_manager_search_result import PackageManagerSearchResult
from data_models.result import Result


class PackageManager(ABC):
    __SUCCESS_RESULT_MESSAGE = "Successfully {install_status} {package_name}"
    __FAILURE_RESULT_MESSAGE = "Failed to {install_status} {package_name}. {reason}"

    @abstractmethod
    def find_package(self, package_name: str) -> List[PackageManagerSearchResult]:
        pass

    @abstractmethod
    def swap_installation_status(self, package: PackageOld) -> Result:
        pass

    def _generate_installation_result_message(self, package: PackageOld, installation_outcome: Result) -> Result:
        install_status = "removed" if package.installed else "installed"
        if installation_outcome.success:
            message = self.__SUCCESS_RESULT_MESSAGE.format(install_status=install_status, package_name=package.name)
        else:
            message = self.__FAILURE_RESULT_MESSAGE.format(
                install_status=install_status, package_name=package.name, reason=installation_outcome.message
            )
        return Result(success=installation_outcome.success, message=message)
