from typing import List, Final

from installer import Installer
from package_installer.package_installer import PackageInstaller

INSTALLATION_SCRIPTS: Final[List[Installer]] = [
    PackageInstaller()
]

for installer in INSTALLATION_SCRIPTS:
    installer.install()
