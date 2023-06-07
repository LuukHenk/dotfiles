
from typing import Dict, List

from data_models.package_info import PackageInfo

class InstallationProgressWidgetProcessor:
    def __init__(self, package_groups: Dict[str, List[PackageInfo]]):
        self.__package_groups = package_groups
