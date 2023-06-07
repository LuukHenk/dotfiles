from typing import List, Dict
from data_models.package_info import PackageInfo
from package_finder.package_finder import PackageFinder


class InstallationWizardWidgetProcessor:
    def __init__(self) -> None:
        self.__package_info_groups: Dict[str, List[PackageInfo]] = PackageFinder().get_package_info()

    @property
    def package_info_groups(self) -> Dict[str, List[PackageInfo]]:
        return self.__package_info_groups
