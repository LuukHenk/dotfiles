


from unittest import TestCase, main
from unittest.mock import Mock, patch, create_autospec

from subprocess import CompletedProcess
from package_installer.data_models.manager_enum import ManagerEnum
from package_installer.data_models.package_info import PackageInfo
from package_installer.data_models.version_enum import Version
from package_installer.package_managers_handlers.apt_package_manager_handler import (
    AptPackageManagerHandler,
)


ABC_CLASS_PATCH_TEMPLATE = "package_installer.package_managers_handlers.package_manager_handler.{}"
MANAGER_CLASS_PATCH_TEMPLATE = "package_installer.package_managers_handlers.apt_package_manager_handler.{}"

class TestAptPackageManagerHandler(TestCase):
    """NOTE: The tester expect that the handler first searches the latest version and secondly searches the installed version"""

    EXAMPLE_INFO_STDOUT_NO_VERSION_INDICATOR = """
Package: python
State: not a real package (virtual)
N: Can't select candidate version from package python as it has no candidate
N: Can't select versions from package 'python' as it is purely virtual
N: No packages found
    """
    
    EXAMPLE_INFO_STDOUT_LATEST_VERSION = """
Package: python3
Version: {}
Priority: important
Section: python
Source: python3-defaults
Origin: Ubuntu
Maintainer: Ubuntu Developers <ubuntu-devel-discuss@lists.ubuntu.com>
Original-Maintainer: Matthias Klose <doko@debian.org>
Bugs: https://bugs.launchpad.net/ubuntu/+filebug
Installed-Size: 92,2 kB
Provides: python3-profiler
Pre-Depends: python3-minimal (= 3.10.6-1~22.04)
Depends: python3.10 (>= 3.10.6-1~), libpython3-stdlib (= 3.10.6-1~22.04)
Suggests: python3-doc (>= 3.10.6-1~22.04), python3-tk (>= 3.10.6-1~), python3-venv (>= 3.10.6-1~22.04)
Replaces: python3-minimal (<< 3.1.2-2)
Homepage: https://www.python.org/
Task: minimal, server-minimal
Download-Size: 22,8 kB
APT-Manual-Installed: no
APT-Sources: http://nl.archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages
Description: interactive high-level object-oriented language (default python3 version)
Python, the high-level, interactive object oriented language,
includes an extensive class library with lots of goodies for
network programming, system administration, sounds and graphics.
.
This package is a dependency package, which depends on Debian's default
Python 3 version (currently v3.10).

N: There is 1 additional record. Please use the '-a' switch to see it
    """

    EXAMPLE_VERSION_STDOUT_NO_VERSION_INDICATOR = """dpkg-query: no packages found match"""
    EXAMPLE_VERSION_STDOUT_INSTALLED_VERSION = """
Desired=Unknown/Install/Remove/Purge/Hold
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name           Version        Architecture Description
+++-==============-==============-============-=========================================================================
ii  python3        {} amd64        interactive high-level object-oriented language (default python3 version)
    """
    RUN_PATCH = MANAGER_CLASS_PATCH_TEMPLATE.format("run_")
    PACKAGE_INFO_PATCH = MANAGER_CLASS_PATCH_TEMPLATE.format("PackageInfo")

    @patch(RUN_PATCH)
    def test_package_version_unsuccessful_exit_status(self, run_patch: Mock):
        # Arrange
        completed_process_mock = create_autospec(CompletedProcess)
        completed_process_mock.returncode = 1
        run_patch.return_value = completed_process_mock
        package_name = "package_name"
        package_manager_handler = AptPackageManagerHandler()
        
        # Act
        package_info = package_manager_handler.find_package(package_name)
        
        # Assert
        self.assertEqual(package_info, [])
        package_info_call = run_patch.call_args_list[0].args[0]
        self.assertEqual(package_info_call, package_manager_handler.INFO_COMMAND + [package_name])
        
    @patch(RUN_PATCH)
    def test_find_latest_package_version_no_version_indicator(self, run_patch: Mock):
        # Arrange
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        latest_version_run_mock.stdout = self.EXAMPLE_INFO_STDOUT_NO_VERSION_INDICATOR
        installed_version_run_mock = create_autospec(CompletedProcess)
        installed_version_run_mock.returncode = 1
        run_patch.side_effect = [latest_version_run_mock, installed_version_run_mock]
        package_name = "python3"
        package_manager_handler = AptPackageManagerHandler()
        
        # Act
        package_info = package_manager_handler.find_package(package_name)
        
        # Assert
        self.assertEqual(package_info, [])
        package_info_call = run_patch.call_args_list[0].args[0]
        self.assertEqual(package_info_call, package_manager_handler.INFO_COMMAND + [package_name])

    @patch(PACKAGE_INFO_PATCH)
    @patch(RUN_PATCH)
    def test_find_latest_package_version_with_success(
        self, run_patch: Mock, package_info_patch: Mock
    ):
        # Arrange
        latest_version = "1.1"
        package_info_mock = create_autospec(PackageInfo)
        package_info_patch.return_value = package_info_mock
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        latest_version_run_mock.stdout = self.EXAMPLE_INFO_STDOUT_LATEST_VERSION.format(latest_version)
        installer_version_run_mock = create_autospec(CompletedProcess)
        installer_version_run_mock.returncode = 1
        run_patch.side_effect = [latest_version_run_mock, installer_version_run_mock]
        package_name = "python3"
        package_manager_handler = AptPackageManagerHandler()
        
        # Act
        package_info = package_manager_handler.find_package(package_name)
        
        # Assert
        package_info_patch.assert_called_once_with(
            name=package_name,
            version=(latest_version, Version.LATEST_STABLE),
            installed=False,
            manager=ManagerEnum.APT,
        )
        self.assertEqual(package_info, [package_info_mock])
        package_info_call = run_patch.call_args_list[0].args[0]
        self.assertEqual(package_info_call, package_manager_handler.INFO_COMMAND + [package_name])
    
    @patch(RUN_PATCH)
    def test_find_installed_version_no_version_indicator(self, run_patch: Mock):
        # Arrange
        installed_version_run_mock = create_autospec(CompletedProcess)
        installed_version_run_mock.returncode = 0
        installed_version_run_mock.stdout = self.EXAMPLE_VERSION_STDOUT_NO_VERSION_INDICATOR
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 1
        run_patch.side_effect = [latest_version_run_mock, installed_version_run_mock]
        package_name = "python3"
        package_manager_handler = AptPackageManagerHandler()
        # Act
        package_info = package_manager_handler.find_package(package_name)
            # Assert
        self.assertEqual(package_info, [])
        package_info_call = run_patch.call_args_list[1].args[0]
        self.assertEqual(package_info_call, package_manager_handler.INSTALLED_COMMAND + [package_name])
        
    @patch(PACKAGE_INFO_PATCH)
    @patch(RUN_PATCH)
    def test_find_installed_version_with_success(self, run_patch: Mock, package_info_patch: Mock):
        # Arrange
        installed_version = "1.2"
        package_info_mock = create_autospec(PackageInfo)
        package_info_patch.return_value = package_info_mock
        installed_version_run_mock = create_autospec(CompletedProcess)
        installed_version_run_mock.returncode = 0
        installed_version_run_mock.stdout = self.EXAMPLE_VERSION_STDOUT_INSTALLED_VERSION.format(installed_version)
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 1
        run_patch.side_effect = [latest_version_run_mock, installed_version_run_mock]
        package_name = "python3"
        package_manager_handler = AptPackageManagerHandler()
        # Act
        package_info = package_manager_handler.find_package(package_name)
        # Assert
        package_info_patch.assert_called_once_with(
            name=package_name,
            version=(installed_version, Version.OTHER),
            installed=True,
            manager=ManagerEnum.APT,
        )        
        self.assertEqual(package_info, [package_info_mock])
        package_info_call = run_patch.call_args_list[1].args[0]
        self.assertEqual(package_info_call, package_manager_handler.INSTALLED_COMMAND + [package_name])

    @patch(PACKAGE_INFO_PATCH)
    @patch(RUN_PATCH)
    def test_latest_package_installed(self, run_patch: Mock, package_info_patch: Mock):
        # Arrange
        latest_version = "1.1.1"
        package_info_mock = create_autospec(PackageInfo)
        package_info_patch.return_value = package_info_mock
        installed_version_run_mock = create_autospec(CompletedProcess)
        installed_version_run_mock.returncode = 0
        installed_version_run_mock.stdout = self.EXAMPLE_VERSION_STDOUT_INSTALLED_VERSION.format(latest_version)
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        latest_version_run_mock.stdout = self.EXAMPLE_INFO_STDOUT_LATEST_VERSION.format(latest_version)
        run_patch.side_effect = [latest_version_run_mock, installed_version_run_mock]
        package_name = "python3"
        package_manager_handler = AptPackageManagerHandler()
        # Act
        package_info = package_manager_handler.find_package(package_name)
        # Assert
        package_info_patch.assert_called_once_with(
            name=package_name,
            version=(latest_version, Version.LATEST_STABLE),
            installed=True,
            manager=ManagerEnum.APT,
        )        
        self.assertEqual(package_info, [package_info_mock])

    @patch(PACKAGE_INFO_PATCH)
    @patch(RUN_PATCH)
    def test_latest_package_not_installed(self, run_patch: Mock, package_info_patch: Mock):
        # Arrange
        latest_version = "1.1.1"
        installed_version = "4.2.0"
        package_info_mock = create_autospec(PackageInfo)
        package_info_patch.return_value = package_info_mock
        installed_version_run_mock = create_autospec(CompletedProcess)
        installed_version_run_mock.returncode = 0
        installed_version_run_mock.stdout = self.EXAMPLE_VERSION_STDOUT_INSTALLED_VERSION.format(installed_version)
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        latest_version_run_mock.stdout = self.EXAMPLE_INFO_STDOUT_LATEST_VERSION.format(latest_version)
        run_patch.side_effect = [latest_version_run_mock, installed_version_run_mock]
        package_name = "python3"
        package_manager_handler = AptPackageManagerHandler()
        # Act
        package_info = package_manager_handler.find_package(package_name)
        # Assert
        latest_version_call = package_info_patch.call_args_list[0]
        latest_version_call.assert_called_once_with(
            name=package_name,
            version=(latest_version, Version.LATEST_STABLE),
            installed=False,
            manager=ManagerEnum.APT,
        )        
        installed_version_call = package_info_patch.call_args_list[1]
        installed_version_call.assert_called_once_with(
            name=package_name,
            version=(installed_version, Version.OTHER),
            installed=True,
            manager=ManagerEnum.APT,
        )     
        self.assertEqual(package_info, [package_info_mock, package_info_mock])
  
if __name__ == '__main__':
    main()