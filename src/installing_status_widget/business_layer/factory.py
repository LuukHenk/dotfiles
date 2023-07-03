from data_layer.package_accessor import PackageAccessor


class Factory:
    def __init__(self, package_accessor: PackageAccessor):
        self.__package_accessor = package_accessor
