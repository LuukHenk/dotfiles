#![allow(dead_code)]

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
        println!("Dummy; installing programs");

    }

    fn copy_file(source: &String, destination: &String) {
        println!("Copying {source} to {destination}");
        let result = copy(source, destination);
        println!("{:#?}", result);
    }
}
