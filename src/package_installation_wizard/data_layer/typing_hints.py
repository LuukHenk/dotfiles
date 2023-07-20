from typing import List, Dict

from data_models.package_old import PackageOld


PackageSets = Dict[str, List[PackageOld]]
NestedPackageGroups = Dict[str, PackageSets]
