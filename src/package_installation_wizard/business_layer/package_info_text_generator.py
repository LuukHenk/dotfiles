from typing import Final

from data_models.package_old import PackageOld

__PACKAGE_TEXT_TEMPLATE: Final[str] = "{install_text}  {package_name} version {version} ({other})"
__INSTALL_TEXT: Final[str] = "Install"
__UNINSTALL_TEXT: Final[str] = "Uninstall"


def generate_package_text(package: PackageOld) -> str:
    return __PACKAGE_TEXT_TEMPLATE.format(
        install_text=__UNINSTALL_TEXT if package.installed else __INSTALL_TEXT,
        package_name=package.name,
        version=package.version.name,
        other=f"{package.manager_name.value.title()} - {package.version.type.value}",
    )
