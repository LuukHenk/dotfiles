
from unittest import TestCase, main
from unittest.mock import Mock, patch, create_autospec

from package_installer.data_models.package_info import PackageInfo
from package_installer.data_models.package_search_query import PackageSearchQuery
from package_installer.package_finder.package_finder import PackageFinder
from package_installer.package_finder.package_managers.apt_package_manager import AptPackageManager
from package_installer.package_finder.package_managers.snap_package_manager import (
    SnapPackageManager,
)


PATCH_TEMPLATE = "package_installer.package_finder.package_finder.{}"

class TestPackageFinder(TestCase):
    APT_PACKAGE_MANAGER_PATCH: str = PATCH_TEMPLATE.format("AptPackageManager")
    SNAP_PACKAGE_MANAGER_PATCH: str = PATCH_TEMPLATE.format("SnapPackageManager")
    
    @patch(APT_PACKAGE_MANAGER_PATCH)
    @patch(SNAP_PACKAGE_MANAGER_PATCH)
    def test_find_package(
        self,
        snap_package_manager_patch: Mock,
        apt_package_manager_patch: Mock
    ) -> None:
        # Arrange
        expected_info_packages = 4
        package_name_1 = "neovim"
        package_name_2 = "nvim"
        query = PackageSearchQuery(
            name="Neovim",
            search_query=[package_name_1, package_name_2]
        )
        package_info_mock = create_autospec(PackageInfo)
        snap_package_manager_mock = create_autospec(SnapPackageManager)
        snap_package_manager_mock.find_package.return_value = [package_info_mock]
        snap_package_manager_patch.return_value = snap_package_manager_mock
        apt_package_manager_mock = create_autospec(AptPackageManager)
        apt_package_manager_mock.find_package.return_value = [package_info_mock]
        apt_package_manager_patch.return_value = apt_package_manager_mock

        # Act
        package_info = PackageFinder().find_package(query)

        # Assert
        self.assertEqual(apt_package_manager_mock.method_calls[0].args[0], package_name_1)
        self.assertEqual(apt_package_manager_mock.method_calls[1].args[0], package_name_2)
        self.assertEqual(snap_package_manager_mock.method_calls[0].args[0], package_name_1)
        self.assertEqual(snap_package_manager_mock.method_calls[1].args[0], package_name_2)
        self.assertEqual(package_info, [package_info_mock]*expected_info_packages)

if __name__ == '__main__':
    main()