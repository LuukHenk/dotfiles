
from typing import List
from package_installer.package_manager_mappers.package_manager_mapper import PackageManagerMapper
from package_installer.package import Package

class AptPackageManagerMapper(PackageManagerMapper):
    def map(self, package_name: str) -> List[Package]:
        return super().map()