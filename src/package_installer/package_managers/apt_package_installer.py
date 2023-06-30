from subprocess import CompletedProcess
from typing import Tuple
from package_installer.package_managers.package_installer import PackageInstaller
from data_models.package_info import PackageInfo
from utils.subprocess_interface import run_
class AptPackageInstaller(PackageInstaller):
    __INSTALLATION_COMMAND = ["sudo", "apt"]
    __SUCCESS_RESULT_MESSAGE = "Package {} successfully {}ed"
    def swap_installation_status(self, package: PackageInfo) -> Tuple[bool, str]:
        installed_text = "install" if package.installed else "uninstall"
        installation_command = [self.__INSTALLATION_COMMAND, installed_text, package.name]
        package_install_run_result: CompletedProcess = run_(installation_command)
        if package_install_run_result.returncode != 0:
            return False, package_install_run_result.stderr
        package.installed = not package.installed
        package.installation_request = False
        return True, self.__SUCCESS_RESULT_MESSAGE.format(package.name, installed_text)
