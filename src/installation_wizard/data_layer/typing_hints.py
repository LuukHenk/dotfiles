from typing import List, Dict

from data_models.package import Package


PackageSets = Dict[str, List[Package]]
NestedPackageGroups = Dict[str, PackageSets]
