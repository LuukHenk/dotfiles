use crate::IoOperationsTrait;
use serde::Deserialize;
use toml::de::Error as TomlError;

#[derive(Deserialize)]
struct Config {
    programs: Vec<String>,
    dotfiles: Vec<Dotfile>,
}

#[derive(Deserialize)]
struct Dotfile {
    name: String,
    repo_path: String,
    deploy_path: String,
}

pub struct ConfigManager {
    config: Config,
}

impl ConfigManager {
    pub fn new(config_str: &str) -> ConfigManager {
        ConfigManager {
            config: ConfigManager::parse_input(config_str),
        }
    }

    pub fn set_dotfiles(&self, io_operations: &mut dyn IoOperationsTrait) {
        for dotfile in self.config.dotfiles.iter() {
            println!("Setting dotfile '{}'", dotfile.name);
            let repo_path = ConfigManager::replace_home_dir_tide(&dotfile.repo_path, io_operations);
            let deploy_path =
                ConfigManager::replace_home_dir_tide(&dotfile.deploy_path, io_operations);
            io_operations.copy_file(&repo_path, &deploy_path);
        }
    }

    pub fn install_programs(&self, io_operations: &mut dyn IoOperationsTrait) {
        println!("Installing programs: {:#?}", &self.config.programs);
        let mut args = Vec::from(["apt-get", "-y", "install"]);
        for program_to_install in self.config.programs.iter() {
            args.push(&program_to_install);
        }
        io_operations.run_command("sudo", args);
    }

    fn replace_home_dir_tide(path: &String, io_operations: &dyn IoOperationsTrait) -> String {
        let home_dir_path = io_operations.get_home_dir_path();
        path.replace("~", &home_dir_path)
    }

    fn parse_input(input: &str) -> Config {
        let result: Result<Config, TomlError> = toml::from_str(input);
        if result.is_err() {
            panic!("Failed to parse the input configuration")
        } else {
            return result.unwrap();
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::{io_operations::FakeIoOperations, ConfigManager};

    #[test]
    #[should_panic]
    fn test_create_config_manager_with_empty_config_str() {
        // Arrange
        let config_str = r#""#;
        // Act
        ConfigManager::new(config_str);
    }

    #[test]
    fn test_create_config_manager_with_required_config_keys() {
        // Arrange
        let config_str = r#"
        programs = []
        dotfiles = []
        "#;
        // Act
        ConfigManager::new(config_str);
    }

    #[test]
    fn test_create_config_manager_with_some_values() {
        // Arrange
        let config_str = r#"
        programs = [
            "python3",
            "htop",
        ]
        [[dotfiles]]
        name="test 1"
        repo_path="conf/test.txt"
        deploy_path="a/result.txt"

        [[dotfiles]]
        name="test home dir"
        repo_path="conf/test.txt"
        deploy_path="a/result.txt"
        "#;
        // Act
        ConfigManager::new(config_str);
    }

    #[test]
    fn test_set_dotfiles_basic() {
        // Arrange
        let config_str = r#"
        programs = [
            "python3",
            "htop",
        ]

        [[dotfiles]]
        name="test set dotfiles"
        repo_path="conf/test.txt"
        deploy_path="a/result.txt"

        [[dotfiles]]
        name="test set dotfiles"
        repo_path="some_location/test.txt"
        deploy_path="someother/result.txt"
        "#;
        let config_manager = ConfigManager::new(config_str);
        let mut io_operations = FakeIoOperations {
            commands_used: Vec::new(),
            copied_files: Vec::new(),
        };
        let mut expected_copies = Vec::new();
        expected_copies.push((String::from("conf/test.txt"), String::from("a/result.txt")));
        expected_copies.push((
            String::from("some_location/test.txt"),
            String::from("someother/result.txt"),
        ));

        // Act
        config_manager.set_dotfiles(&mut io_operations);

        // Assert
        assert_eq!(io_operations.commands_used.len(), 0);
        assert_eq!(io_operations.copied_files, expected_copies);
    }

    #[test]
    fn test_set_dotfiles_with_home_path() {
        // Arrange
        let config_str = r#"
        programs = [
            "python3",
            "htop",
        ]

        [[dotfiles]]
        name="test set dotfiles"
        repo_path="~/test.txt"
        deploy_path="a/result.txt"

        [[dotfiles]]
        name="test set dotfiles"
        repo_path="some_location/test.txt"
        deploy_path="~/result.txt"

        [[dotfiles]]
        name="test set dotfiles"
        repo_path="~/test.txt"
        deploy_path="~/result.txt"
        "#;
        let config_manager = ConfigManager::new(config_str);
        let mut io_operations = FakeIoOperations {
            commands_used: Vec::new(),
            copied_files: Vec::new(),
        };
        let mut expected_copies = Vec::new();
        expected_copies.push((
            String::from("home_dir_path/test.txt"),
            String::from("a/result.txt"),
        ));
        expected_copies.push((
            String::from("some_location/test.txt"),
            String::from("home_dir_path/result.txt"),
        ));
        expected_copies.push((
            String::from("home_dir_path/test.txt"),
            String::from("home_dir_path/result.txt"),
        ));

        // Act
        config_manager.set_dotfiles(&mut io_operations);

        // Assert
        assert_eq!(io_operations.commands_used.len(), 0);
        assert_eq!(io_operations.copied_files, expected_copies);
    }

    #[test]
    fn test_install_programs() {
        // Arrange
        let config_str = r#"
        programs = [
            "python3",
            "htop"
        ]

        [[dotfiles]]
        name="test set dotfiles"
        repo_path="~/test.txt"
        deploy_path="a/result.txt"

        [[dotfiles]]
        name="test set dotfiles"
        repo_path="some_location/test.txt"
        deploy_path="~/result.txt"

        [[dotfiles]]
        name="test set dotfiles"
        repo_path="~/test.txt"
        deploy_path="~/result.txt"
        "#;
        let config_manager = ConfigManager::new(config_str);
        let mut io_operations = FakeIoOperations {
            commands_used: Vec::new(),
            copied_files: Vec::new(),
        };
        let mut expected_commands_used = Vec::new();
        expected_commands_used.push("sudo apt-get -S -y install python3 htop");

        // Act
        config_manager.install_programs(&mut io_operations);

        // Assert
        assert_eq!(
            io_operations.commands_used,
            expected_commands_used
        );
        assert_eq!(io_operations.copied_files.len(), 0);
    }
}
