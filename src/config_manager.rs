#![allow(dead_code)]
use std::process::Command;
use serde::Deserialize;
use std::fs::copy;


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
    config: Config
}

impl ConfigManager{
    pub fn new(config_str: &str) -> ConfigManager {
        let config: Config = toml::from_str(config_str).unwrap();
        ConfigManager{config}
    }

    pub fn set_dotfiles(&self) {
        for dotfile in self.config.dotfiles.iter() {
            ConfigManager::copy_file(&dotfile.repo_path, &dotfile.deploy_path);
        }
    }

    pub fn install_programs(&self) {
        for program_to_install in self.config.programs.iter() {
            let mut command = ConfigManager::create_install_command(program_to_install);
            let result = command.spawn().expect("Failed to install program");
            println!("{:#?}", result)
        }
    }

    fn copy_file(source: &String, destination: &String) {
        println!("Copying {source} to {destination}");
        let result = copy(source, destination);
        println!("{:#?}", result);
    }

    fn create_install_command(program_to_install: &String) -> Command {
        let mut shell_command = Command::new("sudo");
        shell_command.args(["apt-get", "install", "-y", program_to_install]);
        shell_command
    }
}
