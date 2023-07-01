from unittest import TestCase, main
from unittest.mock import Mock, patch, create_autospec

from data_models.package_info import PackageInfo
from data_models.package_search_request import ParsedPackage
from package_finder.package_finder import PackageFinder
from package_finder.package_managers.apt_package_manager_finder import AptPackageManagerFinder
from package_finder.package_managers.snap_package_manager_finder import SnapPackageManagerFinder


PATCH_TEMPLATE = "package_finder.package_finder.{}"


class TestPackageFinder(TestCase):
    APT_PACKAGE_MANAGER_FINDER_PATCH: str = PATCH_TEMPLATE.format("AptPackageManagerFinder")
    SNAP_PACKAGE_MANAGER_FINDER_PATCH: str = PATCH_TEMPLATE.format("SnapPackageManagerFinder")
    GET_PACKAGE_SEARCH_REQUESTS_PATCH: str = PATCH_TEMPLATE.format("get_package_search_requests")

    @patch(GET_PACKAGE_SEARCH_REQUESTS_PATCH)
    @patch(APT_PACKAGE_MANAGER_FINDER_PATCH)
    @patch(SNAP_PACKAGE_MANAGER_FINDER_PATCH)
    def test_get_package_info(
        self,
        snap_package_manager_patch: Mock,
        apt_package_manager_patch: Mock,
        get_package_search_requests_patch: Mock,
    ) -> None:
        # Arrange
        expected_info_packages = 6
        neovim_package_name_1 = "neovim"
        neovim_package_name_2 = "nvim"
        python_package_name = "python"
        get_package_search_requests_patch.return_value = [
            ParsedPackage(
                name="Neovim", search_query=[neovim_package_name_1, neovim_package_name_2], package_group="Neovim"
            ),
            ParsedPackage(name="Python", search_query=[python_package_name], package_group="Python"),
        ]
        package_info_mock = create_autospec(PackageInfo)
        snap_package_manager_mock = create_autospec(SnapPackageManagerFinder)
        snap_package_manager_mock.find_package.return_value = [package_info_mock]
        snap_package_manager_patch.return_value = snap_package_manager_mock
        apt_package_manager_mock = create_autospec(AptPackageManagerFinder)
        apt_package_manager_mock.find_package.return_value = [package_info_mock]
        apt_package_manager_patch.return_value = apt_package_manager_mock

        # Act
        package_info = PackageFinder().get_package_info()

        # Assert
        self.assertEqual(apt_package_manager_mock.method_calls[0].args[0], neovim_package_name_1)
        self.assertEqual(apt_package_manager_mock.method_calls[1].args[0], neovim_package_name_2)
        self.assertEqual(apt_package_manager_mock.method_calls[2].args[0], python_package_name)
        self.assertEqual(snap_package_manager_mock.method_calls[0].args[0], neovim_package_name_1)
        self.assertEqual(snap_package_manager_mock.method_calls[1].args[0], neovim_package_name_2)
        self.assertEqual(snap_package_manager_mock.method_calls[2].args[0], python_package_name)
        self.assertEqual(package_info, [package_info_mock] * expected_info_packages)


if __name__ == "__main__":
    main()
