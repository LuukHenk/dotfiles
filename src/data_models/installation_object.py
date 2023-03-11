
from dataclasses import dataclass

from data_models.package_info import PackageInfo

@dataclass
class InstallationObject:
    package_info: PackageInfo
    configuration: ...