
from typing import List

from package_installer.package_manager_mapper import PackageManagerMapper
from package_installer.package import Package

class SnapPackageManagerMapper(PackageManagerMapper):
    INFO_COMMAND: List[str] = ["snap", "info"]
    
    def map(self, package_name: str) -> List[Package]:
        command = self.INFO_COMMAND + package_name
        return super().map()