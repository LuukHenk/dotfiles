from typing import Final

from data_models.dotfile import Dotfile
from data_models.item import Item
from data_models.package import Package

__DOTFILE_TEXT_TEMPLATE: Final[str] = "{install_text}  {dotfile_name}"
__PACKAGE_TEXT_TEMPLATE: Final[str] = "{install_text}  {package_name} version {version} ({other})"

__INSTALL_TEXT: Final[str] = "Install"
__UNINSTALL_TEXT: Final[str] = "Uninstall"


def generate_text(item: Item):
    if isinstance(item, Dotfile):
        return __generate_dotfile_text(item)
    if isinstance(item, Package):
        return __generate_package_text(item)


def __generate_dotfile_text(dotfile: Dotfile) -> str:
    return __DOTFILE_TEXT_TEMPLATE.format(
        install_text=__get_install_message(dotfile),
        dotfile_name=dotfile.name,
    )


def __generate_package_text(package: Package) -> str:
    return __PACKAGE_TEXT_TEMPLATE.format(
        install_text=__get_install_message(package),
        package_name=package.name,
        version=package.version.name,
        other=f"{package.manager_name.value.title()} - {package.version.type.value}",
    )


def __get_install_message(item: Item) -> str:
    return __UNINSTALL_TEXT if item.installed else __INSTALL_TEXT
