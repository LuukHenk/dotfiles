
use serde::Deserialize;


use crate::IoOperations;

#[derive(Deserialize)]
struct Config {
   programs: Vec<String>,
   dotfiles: Vec<Dotfile>
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

impl ConfigManager{
    pub fn new(config_str: &str) -> ConfigManager {
        let config: Config = toml::from_str(config_str).unwrap();
        ConfigManager{config}
    }

    pub fn set_dotfiles(&self, io_operations: &mut dyn IoOperations) {
        for dotfile in self.config.dotfiles.iter() {
            println!("Setting dotfile '{}'", dotfile.name);
            let repo_path = ConfigManager::replace_home_dir_tide(&dotfile.repo_path, io_operations);
            let deploy_path = ConfigManager::replace_home_dir_tide(&dotfile.deploy_path, io_operations);
            io_operations.copy_file(&repo_path, &deploy_path);
        }
    }

    pub fn install_programs(&self, io_operations: &mut dyn IoOperations) {
        for program_to_install in self.config.programs.iter() {
            io_operations.install_program(program_to_install);

        }
    }

    fn replace_home_dir_tide(path: &String, io_operations: &dyn IoOperations) -> String {
        let home_dir_path = io_operations.get_home_dir_path();
        path.replace("~", &home_dir_path)
    }
}


#[cfg(test)]
mod tests {
    #[test]
    fn test_set_dotfiles_with_no_dotfiles() {
        assert!(false)
    }
}