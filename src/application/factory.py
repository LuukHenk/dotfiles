from configuration_loader.configuration_loader import ConfigurationLoader
from data_layer.package_accessor import PackageAccessor


class Factory:
    def __init__(self):
        package_accessor = PackageAccessor()
        configuration_loader = ConfigurationLoader()
        configuration_loader.load_packages(package_accessor)
