
from typing import List

from unittest import TestCase, main
from unittest.mock import ANY, Mock, patch, create_autospec

from subprocess import CompletedProcess
from package_installer.data_models.manager_enum import ManagerEnum
from package_installer.data_models.package_info import PackageInfo
from package_installer.data_models.version_enum import Version
from package_installer.package_managers_handlers.snap_package_manager_handler import (
    SnapPackageManagerHandler,
    
)


MANAGER_CLASS_PATCH_TEMPLATE = "package_installer.package_managers_handlers.snap_package_manager_handler.{}"
SNAP_SPOTIFY_INFO_TEMPLATE = """
name:      spotify
summary:   Music for everyone
publisher: Spotify✓
store-url: https://snapcraft.io/spotify
contact:   https://community.spotify.com/t5/Desktop-Linux/bd-p/desktop_linux
license:   unset
description: |
  Love music? Play your favorite songs and albums free on Linux with
  Spotify.
  
  Stream the tracks you love instantly, browse the charts or fire up
  readymade playlists in every genre and mood. Radio plays you great
  song after great song, based on your music taste. Discover new music
  too, with awesome playlists built just for you.
  
  Stream Spotify free, with occasional ads, or go Premium.
  
  Free:
  • Play any song, artist, album or playlist instantly
  • Browse hundreds of readymade playlists in every genre and mood
  • Stay on top of the Charts
  • Stream Radio
  • Enjoy podcasts, audiobooks and videos
  • Discover more music with personalized playlists
  
  Premium:
  • Download tunes and play offline
  • Listen ad-free
  • Get even better sound quality
  • Try it free for 30 days, no strings attached
  
  Like us on Facebook: http://www.facebook.com/spotify
  Follow us on Twitter: http://twitter.com/spotify
  
  Note: Spotify for Linux is a labor of love from our engineers that
  wanted to listen to Spotify on their Linux development machines. They
  work on it in their spare time and it is currently not a platform
  that we actively support. The experience may differ from our other
  Spotify Desktop clients, such as Windows and Mac.
commands:
  - spotify
snap-id:      pOBIoZ2LrCB3rDohMxoYGnbN14EHOgD7
{}
"""
TRACKING_TEXT = "tracking:"
VERSION_TEXT = "1.1.84.716.gc5f8b819"
LATEST_STABLE_TEXT = "latest/stable:"
LATEST_STABLE_TEXT_WITH_VERSION = f"{LATEST_STABLE_TEXT}     {VERSION_TEXT}"
LATEST_WITH_CARET = f"{LATEST_STABLE_TEXT}     ^"
SNAP_SPOTIFY_INFO = SNAP_SPOTIFY_INFO_TEMPLATE.format(f"""
{TRACKING_TEXT}
refresh-date: 2023-01-04
channels:
  {LATEST_STABLE_TEXT}
  latest/candidate: 1.1.99.878.g1e4ccc6e 2022-11-22 (62) 184MB -
  latest/beta:      ^                                          
  latest/edge:      1.1.99.878.g1e4ccc6e 2022-11-22 (62) 184MB -
installed:          1.1.84.716.gc5f8b819            (60) 177MB -
""")

class TestAptPackageManagerHandler(TestCase):

    RUN_PATCH = MANAGER_CLASS_PATCH_TEMPLATE.format("run_")
    PACKAGE_INFO_PATCH = MANAGER_CLASS_PATCH_TEMPLATE.format("PackageInfo")

    @patch(RUN_PATCH)
    def test_find_package_with_no_package_info(self, run_patch: Mock) -> None:
        """Test"""
        # Arrange
        completed_process_mock = create_autospec(CompletedProcess)
        completed_process_mock.returncode = 1
        run_patch.return_value = completed_process_mock
        package_name = "package_name"
        package_manager_handler = SnapPackageManagerHandler()
        
        # Act
        package_info = package_manager_handler.find_package(package_name)
        
        # Assert
        self.assertEqual(package_info, [])
        package_info_command = package_manager_handler.INFO_COMMAND + [package_name]
        run_patch.assert_called_once_with(package_info_command)
              
    @patch(RUN_PATCH)
    def test_find_latest_package_versions_with_no_latest_indicator_nor_tracking_indicator(
        self, run_patch: Mock
    ) -> None:
        """Test"""
        # Arrange
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        latest_version_run_mock.stdout = SNAP_SPOTIFY_INFO_TEMPLATE
        run_patch.return_value = latest_version_run_mock
        package_name = "spotify"
        package_manager_handler = SnapPackageManagerHandler()
        
        # Act
        package_info = package_manager_handler.find_package(package_name)

        # Assert
        self.assertEqual(package_info, [])
        
    @patch(RUN_PATCH)
    def test_find_latest_package_versions_with_only_tracking_indicator(
        self, run_patch: Mock
    ) -> None:
        """Test"""

        # Arrange
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        latest_version_run_mock.stdout = SNAP_SPOTIFY_INFO_TEMPLATE.format(TRACKING_TEXT)
        run_patch.return_value = latest_version_run_mock
        package_name = "spotify"
        package_manager_handler = SnapPackageManagerHandler()
        
        # Act
        package_info = package_manager_handler.find_package(package_name)

        # Assert
        self.assertEqual(package_info, [])

    @patch(PACKAGE_INFO_PATCH)
    @patch(RUN_PATCH)
    def test_find_latest_package_versions_with_only_latest_indicator(
        self, run_patch: Mock, package_info_patch: Mock
    ) -> None:
        """Test"""
        # Arrange
        package_info_mock = create_autospec(PackageInfo)
        package_info_patch.return_value = package_info_mock
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        latest_version_run_mock.stdout = SNAP_SPOTIFY_INFO_TEMPLATE.format(
            LATEST_STABLE_TEXT_WITH_VERSION
        )
        run_patch.return_value = latest_version_run_mock
        package_name = "spotify"
        package_manager_handler = SnapPackageManagerHandler()
        
        # Act
        package_info = package_manager_handler.find_package(package_name)

        # Assert
        self.assertEqual(package_info, [package_info_mock])
        package_info_patch.assert_called_once_with(
            name=package_name,
            version=(VERSION_TEXT, Version.LATEST_STABLE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )
        
    @patch(PACKAGE_INFO_PATCH)
    @patch(RUN_PATCH)
    def test_find_latest_package_versions_with_tracking_and_latest_indicator(
        self, run_patch: Mock, package_info_patch: Mock
    ) -> None:
        """Test"""
        # Arrange
        package_info_mock = create_autospec(PackageInfo)
        package_info_patch.return_value = package_info_mock
        
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        latest_version_run_mock.stdout = SNAP_SPOTIFY_INFO_TEMPLATE.format(
            f"{TRACKING_TEXT}   {LATEST_STABLE_TEXT}\n{LATEST_STABLE_TEXT_WITH_VERSION}"
        )
        run_patch.return_value = latest_version_run_mock
        package_name = "spotify"
        package_manager_handler = SnapPackageManagerHandler()
        
        # Act
        package_info = package_manager_handler.find_package(package_name)

        # Assert
        self.assertEqual(package_info, [package_info_mock])
        package_info_patch.assert_called_once_with(
            name=package_name,
            version=(VERSION_TEXT, Version.LATEST_STABLE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )
        
    @patch(PACKAGE_INFO_PATCH)
    @patch(RUN_PATCH)    
    def test_find_latest_package_versions_with_duplicate_versions(
        self, run_patch: Mock, package_info_patch: Mock
    ) -> None:
        """Test"""
        # Arrange
        package_info_mock = create_autospec(PackageInfo)
        package_info_patch.return_value = package_info_mock
        
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        latest_version_run_mock.stdout = SNAP_SPOTIFY_INFO_TEMPLATE.format(
            f"{LATEST_STABLE_TEXT_WITH_VERSION}\nlatest/edge:     {VERSION_TEXT}"
        )
        run_patch.return_value = latest_version_run_mock
        package_name = "spotify"
        package_manager_handler = SnapPackageManagerHandler()
        
        # Act
        package_info = package_manager_handler.find_package(package_name)

        # Assert
        self.assertEqual(package_info, [package_info_mock])
        package_info_patch.assert_called_once_with(
            name=package_name,
            version=(VERSION_TEXT, Version.LATEST_STABLE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )

    @patch(RUN_PATCH)
    def test_find_latest_package_versions_with_caret_in_version_name(
        self, run_patch: Mock
    ) -> None:
        """Test"""
        # Arrange
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        latest_version_run_mock.stdout = SNAP_SPOTIFY_INFO_TEMPLATE.format(
            LATEST_WITH_CARET
        )
        run_patch.return_value = latest_version_run_mock
        package_name = "spotify"
        package_manager_handler = SnapPackageManagerHandler()
        
        # Act
        package_info = package_manager_handler.find_package(package_name)

        # Assert
        self.assertEqual(package_info, [])

    @patch(PACKAGE_INFO_PATCH)
    @patch(RUN_PATCH)   
    def test_match_stable_version(
        self, run_patch: Mock, package_info_patch: Mock
    ) -> None:
        """Test"""
        # Arrange
        package_info_mock = create_autospec(PackageInfo)
        package_info_patch.return_value = package_info_mock
        
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        latest_version_run_mock.stdout = SNAP_SPOTIFY_INFO_TEMPLATE.format(
            f"{LATEST_STABLE_TEXT_WITH_VERSION}"
        )
        run_patch.return_value = latest_version_run_mock
        package_name = "spotify"
        package_manager_handler = SnapPackageManagerHandler()        
        # Act
        package_info = package_manager_handler.find_package(package_name)

        # Assert
        self.assertEqual(package_info, [package_info_mock])
        package_info_patch.assert_called_once_with(
            name=package_name,
            version=(VERSION_TEXT, Version.LATEST_STABLE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )     
        
    @patch(PACKAGE_INFO_PATCH)
    @patch(RUN_PATCH)   
    def test_match_candiate_version(
        self, run_patch: Mock, package_info_patch: Mock
    ) -> None:
        """Test"""
        # Arrange
        package_info_mock = create_autospec(PackageInfo)
        package_info_patch.return_value = package_info_mock
        
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        latest_version_run_mock.stdout = SNAP_SPOTIFY_INFO_TEMPLATE.format(
            f"latest/candidate:        {VERSION_TEXT}"
        )
        run_patch.return_value = latest_version_run_mock
        package_name = "spotify"
        package_manager_handler = SnapPackageManagerHandler()        
        # Act
        package_info = package_manager_handler.find_package(package_name)

        # Assert
        self.assertEqual(package_info, [package_info_mock])
        package_info_patch.assert_called_once_with(
            name=package_name,
            version=(VERSION_TEXT, Version.LATEST_CANDIDATE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )     

        
    @patch(PACKAGE_INFO_PATCH)
    @patch(RUN_PATCH)   
    def test_match_beta_version(
        self, run_patch: Mock, package_info_patch: Mock
    ) -> None:
        """Test"""
        package_info_mock = create_autospec(PackageInfo)
        package_info_patch.return_value = package_info_mock
        
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        latest_version_run_mock.stdout = SNAP_SPOTIFY_INFO_TEMPLATE.format(
            f"latest/beta:        {VERSION_TEXT}"
        )
        run_patch.return_value = latest_version_run_mock
        package_name = "spotify"
        package_manager_handler = SnapPackageManagerHandler()        
        # Act
        package_info = package_manager_handler.find_package(package_name)

        # Assert
        self.assertEqual(package_info, [package_info_mock])
        package_info_patch.assert_called_once_with(
            name=package_name,
            version=(VERSION_TEXT, Version.LATEST_BETA),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )     

        
    @patch(PACKAGE_INFO_PATCH)
    @patch(RUN_PATCH)   
    def test_match_edge_version(
        self, run_patch: Mock, package_info_patch: Mock
    ) -> None:
        """Test"""
        package_info_mock = create_autospec(PackageInfo)
        package_info_patch.return_value = package_info_mock
        
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        latest_version_run_mock.stdout = SNAP_SPOTIFY_INFO_TEMPLATE.format(
            f"latest/edge:        {VERSION_TEXT}"
        )
        run_patch.return_value = latest_version_run_mock
        package_name = "spotify"
        package_manager_handler = SnapPackageManagerHandler()        
        # Act
        package_info = package_manager_handler.find_package(package_name)

        # Assert
        self.assertEqual(package_info, [package_info_mock])
        package_info_patch.assert_called_once_with(
            name=package_name,
            version=(VERSION_TEXT, Version.LATEST_EDGE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )     

        
    @patch(PACKAGE_INFO_PATCH)
    @patch(RUN_PATCH)   
    def test_match_other_version(
        self, run_patch: Mock, package_info_patch: Mock
    ) -> None:
        """Test"""
        package_info_mock = create_autospec(PackageInfo)
        package_info_patch.return_value = package_info_mock
        
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        latest_version_run_mock.stdout = SNAP_SPOTIFY_INFO_TEMPLATE.format(
            f"latest/some version 1.83.4:        {VERSION_TEXT}"
        )
        run_patch.return_value = latest_version_run_mock
        package_name = "spotify"
        package_manager_handler = SnapPackageManagerHandler()        
        # Act
        package_info = package_manager_handler.find_package(package_name)

        # Assert
        self.assertEqual(package_info, [package_info_mock])
        package_info_patch.assert_called_once_with(
            name=package_name,
            version=(VERSION_TEXT, Version.OTHER),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )     

    @patch(PACKAGE_INFO_PATCH)
    @patch(RUN_PATCH)           
    def test_version_formatting_when_there_is_no_spacing(
        self, run_patch: Mock, package_info_patch: Mock
    ) -> None:
        """Test"""
        # Arrange
        package_info_mock = create_autospec(PackageInfo)
        package_info_patch.return_value = package_info_mock
        
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        version_text = "v0.9.0-613+gef18c9f9b"
        latest_version_run_mock.stdout = SNAP_SPOTIFY_INFO_TEMPLATE.format(
            f"{LATEST_STABLE_TEXT}        {version_text}"
        )
        run_patch.return_value = latest_version_run_mock
        package_name = "spotify"
        package_manager_handler = SnapPackageManagerHandler()        
        # Act
        package_info = package_manager_handler.find_package(package_name)

        # Assert
        self.assertEqual(package_info, [package_info_mock])
        package_info_patch.assert_called_once_with(
            name=package_name,
            version=(version_text, Version.LATEST_STABLE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )  

    @patch(PACKAGE_INFO_PATCH)
    @patch(RUN_PATCH)   
    def test_version_formatting_with_single_spacing(
        self, run_patch: Mock, package_info_patch: Mock
    ) -> None:
        """Test"""
        # Arrange
        package_info_mock = create_autospec(PackageInfo)
        package_info_patch.return_value = package_info_mock
        
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        version_text = "v0.9.0-613+gef18c9f9b"
        text_after_spacing = "1.1.99.878.g1e4ccc6e"
        latest_version_run_mock.stdout = SNAP_SPOTIFY_INFO_TEMPLATE.format(
            f"{LATEST_STABLE_TEXT}        {version_text} {text_after_spacing}"
        )
        run_patch.return_value = latest_version_run_mock
        package_name = "spotify"
        package_manager_handler = SnapPackageManagerHandler()        
        # Act
        package_info = package_manager_handler.find_package(package_name)

        # Assert
        self.assertEqual(package_info, [package_info_mock])
        package_info_patch.assert_called_once_with(
            name=package_name,
            version=(version_text, Version.LATEST_STABLE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )  
        
    @patch(PACKAGE_INFO_PATCH)
    @patch(RUN_PATCH)   
    def test_version_formatting_with_many_spacings(
        self, run_patch: Mock, package_info_patch: Mock
    ) -> None:
        """Test"""
        # Arrange
        package_info_mock = create_autospec(PackageInfo)
        package_info_patch.return_value = package_info_mock
        
        latest_version_run_mock = create_autospec(CompletedProcess)
        latest_version_run_mock.returncode = 0
        version_text = "v0.9.0-613+gef18c9f9b"
        text_after_spacing = "1.1.99.878.g1e4ccc6e"
        latest_version_run_mock.stdout = SNAP_SPOTIFY_INFO_TEMPLATE.format(
            f"{LATEST_STABLE_TEXT}        {version_text}  {text_after_spacing} {text_after_spacing}"
        )
        run_patch.return_value = latest_version_run_mock
        package_name = "spotify"
        package_manager_handler = SnapPackageManagerHandler()        
        # Act
        package_info = package_manager_handler.find_package(package_name)

        # Assert
        self.assertEqual(package_info, [package_info_mock])
        package_info_patch.assert_called_once_with(
            name=package_name,
            version=(version_text, Version.LATEST_STABLE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )  

    def test_find_installed_version_when_there_is_no_installed_indicator(self) -> None:
        """Test"""

    def test_find_installed_version_when_there_is_an_installed_indicator(self) -> None:
        """Test"""


    def test_generate_package_info_when_non_is_installed(self) -> None:
        """Test"""

    def test_generat_package_info_when_installed_not_in_latest_versions(self) -> None:
        """Test"""

    def test_generat_package_info_when_installed_in_latest_versions(self) -> None:
        """Test"""

if __name__ == '__main__':
    main()