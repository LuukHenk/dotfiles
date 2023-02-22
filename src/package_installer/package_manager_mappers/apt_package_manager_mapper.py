
from typing import List
from package_installer.package_manager_mappers.package_manager_mapper import PackageManagerMapper
from package_installer.package_info import PackageInfo

class AptPackageManagerMapper(PackageManagerMapper):
    def map(self, package_name: str) -> List[PackageInfo]:
        return super().map()