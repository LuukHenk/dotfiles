


from typing import List
from data_models.package_info import PackageInfo
from package_finder.package_finder import PackageFinder


class InstallationWizardWidgetProcessor:
    def __init__(self) -> None:
        self.__package_info: List[PackageInfo] = PackageFinder().get_package_info()
        print(self.__package_info)