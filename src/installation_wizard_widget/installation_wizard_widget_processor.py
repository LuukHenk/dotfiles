from typing import List, Dict
from data_models.package_info import PackageInfo
from package_finder.package_finder import PackageFinder


class InstallationWizardWidgetProcessor:
    def __init__(self) -> None:
        self.__package_info: Dict[str, List[PackageInfo]] = PackageFinder().get_package_info()

    @property
    def package_info(self) -> Dict[str, List[PackageInfo]]:
        return self.__package_info

    def get_package_groups(self) -> List[str]:
        return list(self.__package_info)

    def get_group_package_info(self, group: str) -> List[PackageInfo]:
        return self.__package_info[group] if group in self.__package_info else []
