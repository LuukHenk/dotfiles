
from unittest import TestCase, main
from unittest.mock import Mock, patch, create_autospec

from subprocess import CompletedProcess

from package_installer.version_enum import Version
from package_installer.package_manager_mappers.snap_package_manager_mapper import SnapPackageManagerMapper


FILE_PATH = "package_installer.package_manager_mappers.snap_package_manager_mapper.{}"
EXAMPLE_NON_INSTALLED_PACKAGE = """
name:      pogo
summary:   A fast and minimalist audio player for Linux
publisher: Snapcrafters
store-url: https://snapcraft.io/pogo
contact:   https://github.com/ymauray/pogo-snap/issues
license:   GPL-2.0-or-later
description: something
    multiline
snap-id: GiAsN8tINHLs3TYGVBB7dXNethkuesf5
channels:
  latest/stable:    v1.0.1 2021-09-23 (5)  93MB -
  latest/candidate: ↑                           
  latest/beta:      v1.0.1 2021-09-15 (5)  93MB -
  latest/edge:      v1.0.1 2021-09-09 (3) 116MB -
"""
EXAMPLE_INSTALLED_PACKAGE = """
name:      spotify
summary:   Music for everyone
publisher: Spotify✓
store-url: https://snapcraft.io/spotify
contact:   https://community.spotify.com/t5/Desktop-Linux/bd-p/desktop_linux
license:   unset
description: |
  somthing multiline
  
Note: multiline
  note
Commands:
  - spotify
snap-id:      pOBIoZ2LrCB3rDohMxoYGnbN14EHOgD7
tracking:     latest/stable
refresh-date: 49 days ago, at 16:56 CET
channels:
  latest/stable:    1.1.84.716.gc5f8b819 2022-04-27 (60) 177MB -
  latest/candidate: 1.1.99.878.g1e4ccc6e 2022-11-22 (62) 184MB -
  latest/beta:      ↑                                          
  latest/edge:      1.1.99.878.g1e4ccc6e 2022-11-22 (62) 184MB -
installed:          1.1.84.716.gc5f8b819            (60) 177MB -
"""
EXAMPLE_INSTALLED_PACKAGE_WHERE_INSTALLED_MISMATCHES_LATEST = """
name:      spotify
summary:   Music for everyone
publisher: Spotify✓
store-url: https://snapcraft.io/spotify
contact:   https://community.spotify.com/t5/Desktop-Linux/bd-p/desktop_linux
license:   unset
description: |
  somthing multiline
  
Note: multiline
  note
Commands:
  - spotify
snap-id:      pOBIoZ2LrCB3rDohMxoYGnbN14EHOgD7
tracking:     latest/stable
refresh-date: 49 days ago, at 16:56 CET
channels:
  latest/stable:    1.1.84.716.gc5f8b819 2022-04-27 (60) 177MB -
  latest/candidate: 1.1.99.878.g1e4ccc6e 2022-11-22 (62) 184MB -
  latest/beta:      ↑                                          
  latest/edge:      1.1.99.878.g1e4ccc6e 2022-11-22 (62) 184MB -
installed:          1.1.20.716.gc5f8b819            (60) 177MB -
"""
EXAMPLE_INSTALLED_PACKAGE_WITH_MANY_CHANNELS = """
name:      juju
summary:   Juju - a model-driven operator lifecycle manager for K8s and machines
publisher: Canonical✓
store-url: https://snapcraft.io/juju
contact:   https://canonical.com/
license:   AGPL-3.0
description: |
  A model-driven **universal operator lifecycle manager** for multi cloud and hybrid cloud
snap-id: e2CPHpB1fUxcKtCyJTsm5t3hN9axJ0yj
channels:
  2.9/stable:       2.9.38            2023-01-17 (21790) 97MB classic
  2.9/candidate:    2.9.40            2023-02-17 (22264) 97MB classic
  2.9/beta:         ↑                                         
  2.9/edge:         2.9.40-af42851    2023-02-16 (22257) 97MB classic
  latest/stable:    2.9.38            2023-01-17 (21790) 97MB classic
  latest/candidate: 2.9.40            2023-02-17 (22264) 97MB classic
  latest/beta:      ↑                                         
  latest/edge:      3.1.1-a32a37c     2023-02-14 (22241) 76MB -
  3.2/stable:       –                                         
  3.2/candidate:    –                                         
  3.2/beta:         –                                         
  3.2/edge:         3.2-beta1-37c2ddd 2023-02-09 (22225) 76MB -
  3.1/stable:       3.1.0             2023-02-05 (22136) 76MB -
  3.1/candidate:    ↑                                         
  3.1/beta:         ↑                                         
  3.1/edge:         3.1.1-a32a37c     2023-02-14 (22241) 76MB -
  3.0/stable:       3.0.3             2023-02-15 (22197) 76MB -
  3.0/candidate:    ↑                                         
  3.0/beta:         ↑                                         
  3.0/edge:         3.0.4-633c9b5     2023-02-16 (22253) 76MB -
  2.8/stable:       2.8.13            2021-11-11 (17665) 74MB classic
  2.8/candidate:    ↑                                         
  2.8/beta:         ↑                                         
  2.8/edge:         ↑  
installed:          2.8.13            2021-11-11 (17665) 74MB classic
"""
class TestSnapPackageManagerMapper(TestCase):
    
    @patch(FILE_PATH.format("run"))
    def test_map_with_invalid_return_code(self, run_patch: Mock):
        # Arrange
        package_name = "package name"
        process_result = create_autospec(CompletedProcess)
        process_result.returncode = 1
        run_patch.return_value = process_result
        snap_package_manager = SnapPackageManagerMapper()
        
        # Act
        package_info = snap_package_manager.map(package_name)
        
        # Assert
        self.assertEqual(package_info.name, package_name)
        self.assertFalse(package_info.found)
        self.assertFalse(package_info.installed)
        self.assertIsNone(package_info.installed_version)
        
    @patch(FILE_PATH.format("run"))
    def test_map_found_but_not_installed(self, run_patch: Mock):
        # Arrange
        package_name = "package name"
        process_result = create_autospec(CompletedProcess)
        process_result.returncode = 0
        process_result.stdout = EXAMPLE_NON_INSTALLED_PACKAGE
        run_patch.return_value = process_result
        snap_package_manager = SnapPackageManagerMapper()
        
        # Act
        package_info = snap_package_manager.map(package_name)
        
        # Assert
        self.assertEqual(package_info.name, package_name)
        self.assertTrue(package_info.found)
        self.assertFalse(package_info.installed)
        self.assertIsNone(package_info.installed_version)
        
    @patch(FILE_PATH.format("run"))    
    def test_map_found_and_installed_latest_stable(self, run_patch: Mock):
        # Arrange
        package_name = "package name"
        process_result = create_autospec(CompletedProcess)
        process_result.returncode = 0
        process_result.stdout = EXAMPLE_INSTALLED_PACKAGE
        run_patch.return_value = process_result
        snap_package_manager = SnapPackageManagerMapper()
        
        # Act
        package_info = snap_package_manager.map(package_name)
        
        # Assert
        self.assertEqual(package_info.name, package_name)
        self.assertTrue(package_info.found)
        self.assertTrue(package_info.installed)
        self.assertEqual(package_info.installed_version[0], "1.1.84.716.gc5f8b819")
        self.assertEqual(package_info.installed_version[1], Version.LATEST_STABLE)

    @patch(FILE_PATH.format("run"))    
    def test_map_found_and_installed_other_version(self, run_patch: Mock):
        # Arrange
        package_name = "package name"
        process_result = create_autospec(CompletedProcess)
        process_result.returncode = 0
        process_result.stdout = EXAMPLE_INSTALLED_PACKAGE_WHERE_INSTALLED_MISMATCHES_LATEST
        run_patch.return_value = process_result
        snap_package_manager = SnapPackageManagerMapper()
        
        # Act
        package_info = snap_package_manager.map(package_name)
        
        # Assert
        self.assertEqual(package_info.name, package_name)
        self.assertTrue(package_info.found)
        self.assertTrue(package_info.installed)
        self.assertEqual(package_info.installed_version[0], "1.1.20.716.gc5f8b819")
        self.assertEqual(package_info.installed_version[1], Version.OTHER)
    
    @patch(FILE_PATH.format("run")) 
    def test_map_found_and_installed_with_many_channels_available(self, run_patch: Mock):
        # Arrange
        package_name = "package name"
        process_result = create_autospec(CompletedProcess)
        process_result.returncode = 0
        process_result.stdout = EXAMPLE_INSTALLED_PACKAGE_WITH_MANY_CHANNELS
        run_patch.return_value = process_result
        snap_package_manager = SnapPackageManagerMapper()
        
        # Act
        package_info = snap_package_manager.map(package_name)
        
        # Assert
        self.assertEqual(package_info.name, package_name)
        self.assertTrue(package_info.found)
        self.assertTrue(package_info.installed)
        self.assertEqual(package_info.installed_version[0], "2.8.13")
        self.assertEqual(package_info.installed_version[1], Version.OTHER)
    

if __name__ == '__main__':
    main()