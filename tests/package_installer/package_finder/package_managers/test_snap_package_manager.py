
from typing import List, Tuple

from unittest import TestCase, main
from unittest.mock import ANY, Mock, patch, create_autospec

from subprocess import CompletedProcess
from package_installer.data_models.manager_enum import ManagerEnum
from package_installer.data_models.package_info import PackageInfo
from package_installer.data_models.version_enum import Version
from package_installer.package_finder.package_managers.snap_package_manager import (
    SnapPackageManager,
)


MANAGER_CLASS_PATCH_TEMPLATE = "package_installer.package_finder.package_managers.snap_package_manager.{}"

class TestAptPackageManager(TestCase):

    RUN_PATCH = MANAGER_CLASS_PATCH_TEMPLATE.format("run_")
    PACKAGE_INFO_PATCH = MANAGER_CLASS_PATCH_TEMPLATE.format("PackageInfo")

    @patch(RUN_PATCH)
    def test_find_package_with_no_package_info(self, run_patch: Mock) -> None:
        # Arrange
        completed_process_mock = create_autospec(CompletedProcess)
        completed_process_mock.returncode = 1
        run_patch.return_value = completed_process_mock
        package_name = "package_name"
        package_manager_handler = SnapPackageManager()
        
        # Act
        package_info = package_manager_handler.find_package(package_name)
        
        # Assert
        self.assertEqual(package_info, [])
        package_info_command = package_manager_handler.INFO_COMMAND + [package_name]
        run_patch.assert_called_once_with(package_info_command)
              
    def test_find_latest_package_versions_with_no_text_of_interest(self) -> None:
        # Arrange
        # Act
        package_info, _package_info_patch = self.__find_package(generate_spotify_info_text())
        # Assert
        self.assertEqual(package_info, [])
        
    def test_find_latest_package_versions_with_only_tracking_indicator(self) -> None:
        # Arrange
        text = generate_spotify_info_text(tracking_text=DEFAULT_TRACKING_TEXT)

        # Act
        package_info, _package_info_patch = self.__find_package(text)

        # Assert
        self.assertEqual(package_info, [])

    def test_find_latest_package_versions_with_only_latest_indicator(self) -> None:
        # Arrange
        text = generate_spotify_info_text(channel_text=DEFAULT_CHANNELS_TEXT)

        # Act
        package_info, package_info_patch = self.__find_package(text)

        # Assert
        self.assertEqual(package_info, [PACKAGE_INFO_MOCK])
        package_info_patch.assert_called_once_with(
            name=PACKAGE_NAME,
            version=(DEFAULT_VERSION, Version.LATEST_STABLE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )
        
    def test_find_latest_package_versions_with_tracking_and_latest_indicator(self) -> None:
        # Arrange
        text = generate_spotify_info_text(
            tracking_text=DEFAULT_TRACKING_TEXT,
            channel_text=DEFAULT_CHANNELS_TEXT
        )
        
        # Act
        package_info, package_info_patch = self.__find_package(text)

        # Assert
        self.assertEqual(package_info, [PACKAGE_INFO_MOCK])
        package_info_patch.assert_called_once_with(
            name=PACKAGE_NAME,
            version=(DEFAULT_VERSION, Version.LATEST_STABLE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )
    
    def test_find_latest_package_versions_with_duplicate_versions(self) -> None:
        # Arrange
        duplicate_text = f"{DEFAULT_VERSION} 2022-04-27 (60) 177MB -"
        channel_text = f"""latest/stable: {duplicate_text}\nlatest/edge: {duplicate_text}"""
        text = generate_spotify_info_text(channel_text=channel_text)
        
        # Act
        package_info, package_info_patch = self.__find_package(text)

        # Assert
        self.assertEqual(package_info, [PACKAGE_INFO_MOCK])
        package_info_patch.assert_called_once_with(
            name=PACKAGE_NAME,
            version=(DEFAULT_VERSION, Version.LATEST_STABLE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )

    def test_find_latest_package_versions_with_caret_in_version_name(self) -> None:
        # Arrange
        text = generate_spotify_info_text(channel_text="latest/stable: ^")
        
        # Act
        package_info, _package_info_patch = self.__find_package(text)

        # Assert
        self.assertEqual(package_info, [])
   
    def test_match_candiate_version(self) -> None:
        # Arrange
        text = generate_spotify_info_text(channel_text=f"latest/candidate: {DEFAULT_VERSION}")
        
        # Act
        package_info, package_info_patch = self.__find_package(text)

        # Assert
        self.assertEqual(package_info, [PACKAGE_INFO_MOCK])
        package_info_patch.assert_called_once_with(
            name=PACKAGE_NAME,
            version=(DEFAULT_VERSION, Version.LATEST_CANDIDATE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )     

    def test_match_beta_version(self) -> None:
        # Arrange
        text = generate_spotify_info_text(channel_text=f"latest/beta: {DEFAULT_VERSION}")
    
        # Act
        package_info, package_info_patch = self.__find_package(text)

        # Assert
        self.assertEqual(package_info, [PACKAGE_INFO_MOCK])
        package_info_patch.assert_called_once_with(
            name=PACKAGE_NAME,
            version=(DEFAULT_VERSION, Version.LATEST_BETA),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )     

    def test_match_edge_version(self) -> None:
        # Arrange
        text = generate_spotify_info_text(channel_text=f"latest/edge: {DEFAULT_VERSION}")
        
        # Act
        package_info, package_info_patch = self.__find_package(text)

        # Assert
        self.assertEqual(package_info, [PACKAGE_INFO_MOCK])
        package_info_patch.assert_called_once_with(
            name=PACKAGE_NAME,
            version=(DEFAULT_VERSION, Version.LATEST_EDGE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )     

    def test_match_other_version(self) -> None:
        text = generate_spotify_info_text(
            channel_text=f"latest/som eversion 1983094.: {DEFAULT_VERSION}"
        )
        
        # Act
        package_info, package_info_patch = self.__find_package(text)

        # Assert
        self.assertEqual(package_info, [PACKAGE_INFO_MOCK])
        package_info_patch.assert_called_once_with(
            name=PACKAGE_NAME,
            version=(DEFAULT_VERSION, Version.OTHER),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )     
    
    def test_version_formatting_when_there_is_no_spacing(self) -> None:
        # Arrange
        version_text = "v0.9.0-613+gef18c9f9b"
        text = generate_spotify_info_text(
            channel_text=f"latest/stable:        {version_text}"
        )
        
        # Act
        package_info, package_info_patch = self.__find_package(text)

        # Assert
        self.assertEqual(package_info, [PACKAGE_INFO_MOCK])
        package_info_patch.assert_called_once_with(
            name=PACKAGE_NAME,
            version=(version_text, Version.LATEST_STABLE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )  

    def test_version_formatting_with_single_spacing(self) -> None:
        # Arrange
        version_text = "v0.9.0-613+gef18c9f9b"
        text_after_spacing = "1.1.99.878.g1e4ccc6e"
        text = generate_spotify_info_text(
            channel_text=f"latest/stable:        {version_text} {text_after_spacing}"
        )
        
        # Act
        package_info, package_info_patch = self.__find_package(text)

        # Assert
        self.assertEqual(package_info, [PACKAGE_INFO_MOCK])
        package_info_patch.assert_called_once_with(
            name=PACKAGE_NAME,
            version=(version_text, Version.LATEST_STABLE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )  
        
    def test_version_formatting_with_many_spacings(self) -> None:
        # Arrange
        version_text = "v0.9.0-613+gef18c9f9b"
        text_after_spacing = "1.1.99.878.g1e4ccc6e"
        text = generate_spotify_info_text(
            channel_text=f"latest/stable:        {version_text} {text_after_spacing}   {text_after_spacing}"
        )
        
        # Act
        package_info, package_info_patch = self.__find_package(text)

        # Assert
        self.assertEqual(package_info, [PACKAGE_INFO_MOCK])
        package_info_patch.assert_called_once_with(
            name=PACKAGE_NAME,
            version=(version_text, Version.LATEST_STABLE),
            installed=ANY,
            manager=ManagerEnum.SNAP
        )  

    def test_find_installed_version_when_non_is_installed(self) -> None:
        # Arrange
        text = generate_spotify_info_text(channel_text=DEFAULT_CHANNELS_TEXT)

        # Act
        package_info, package_info_patch = self.__find_package(text)

        # Assert
        self.assertEqual(package_info, [PACKAGE_INFO_MOCK])
        package_info_patch.assert_called_once_with(
            name=PACKAGE_NAME,
            version=ANY,
            installed=False,
            manager=ManagerEnum.SNAP
        )    

    def test_find_installed_version_when_there_is_an_installed_indicator(self) -> None:
        # Arrange
        text = generate_spotify_info_text(
            channel_text=DEFAULT_CHANNELS_TEXT,
            installed_text=DEFAULT_INSTALLED_TEXT
        )

        # Act
        package_info, package_info_patch = self.__find_package(text)

        # Assert
        self.assertEqual(package_info, [PACKAGE_INFO_MOCK])
        package_info_patch.assert_called_once_with(
            name=PACKAGE_NAME,
            version=ANY,
            installed=True,
            manager=ManagerEnum.SNAP
        )    

    def test_generat_package_info_when_installed_not_in_latest_versions(self) -> None:
        # Arrange
        text = generate_spotify_info_text(
            channel_text="latest/beta: v1.0",
            installed_text=DEFAULT_INSTALLED_TEXT
        )

        # Act
        package_info, package_info_patch = self.__find_package(text)

        # Assert
        self.assertEqual(package_info, [PACKAGE_INFO_MOCK, PACKAGE_INFO_MOCK])
        package_info_patch.assert_called_with(
            name=PACKAGE_NAME,
            version=(DEFAULT_VERSION, Version.OTHER),
            installed=True,
            manager=ManagerEnum.SNAP
        ) 
        
    def test_generat_package_info_when_installed_in_latest_versions(self) -> None:
        # Arrange
        text = generate_spotify_info_text(
            channel_text=f"latest/beta: {DEFAULT_VERSION}",
            installed_text=f"installed: {DEFAULT_VERSION}"
        )

        # Act
        package_info, package_info_patch = self.__find_package(text)

        # Assert
        self.assertEqual(package_info, [PACKAGE_INFO_MOCK])
        package_info_patch.assert_called_once_with(
            name=PACKAGE_NAME,
            version=(DEFAULT_VERSION, Version.LATEST_BETA),
            installed=True,
            manager=ManagerEnum.SNAP
        ) 
    def __find_package(self, snap_info_text: str) -> Tuple[List[PackageInfo], Mock]:
        """Returns: the found package info, and the package info patch"""
        # Arrange
        run_mock = create_autospec(CompletedProcess)
        run_mock.stdout = snap_info_text
        run_mock.returncode = 0
        package_name = PACKAGE_NAME
        package_manager_handler = SnapPackageManager()        
        # Act
        with (
            patch(self.RUN_PATCH) as run_patch,
            patch(self.PACKAGE_INFO_PATCH) as package_info_patch, 
        ):
            run_patch.return_value = run_mock
            package_info_patch.return_value = PACKAGE_INFO_MOCK
            package_info = package_manager_handler.find_package(package_name)

        # Assert
        return package_info, package_info_patch # type: ignore

PACKAGE_INFO_MOCK = create_autospec(PackageInfo)
PACKAGE_NAME = "spotify"
DEFAULT_VERSION = "1.1.84.716.gc5f8b819"
DEFAULT_TRACKING_TEXT = "tracking:     latest/stable"
DEFAULT_CHANNELS_TEXT = f"latest/stable:    {DEFAULT_VERSION} 2022-04-27 (60) 177MB -"
DEFAULT_INSTALLED_TEXT = f"installed:          {DEFAULT_VERSION}            (60) 177MB -"

def generate_spotify_info_text(
    tracking_text: str="",
    channel_text: str="",
    installed_text: str="",
    
) -> str:
    return f"""
name:      {PACKAGE_NAME}
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
{tracking_text}
refresh-date: 2023-01-04
channels:
  {channel_text}
{installed_text}
"""
if __name__ == '__main__':
    main()