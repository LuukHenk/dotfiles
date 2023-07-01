from typing import Final

from old.data_models.package_info import PackageInfo

PACKAGE_TEXT_TEMPLATE: Final[str] = "{install_text}  {package_name} version {version} ({other})"
INSTALL_TEXT: Final[str] = "Install"
UNINSTALL_TEXT: Final[str] = "Uninstall"


def generate_package_info_text(package_info: PackageInfo) -> str:
    return PACKAGE_TEXT_TEMPLATE.format(
        install_text=UNINSTALL_TEXT if package_info.installed else INSTALL_TEXT,
        package_name=package_info.name,
        version=package_info.version[0],
        other=f"{package_info.manager.title()} - {package_info.version[1].value}",
    )
