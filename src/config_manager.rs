use std::process::Command;
use serde::Deserialize;
use std::fs::copy;
use home::home_dir;

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

    pub fn set_dotfiles(&self) {
        for dotfile in self.config.dotfiles.iter() {
            println!("Setting dotfile '{}'", dotfile.name);
            let repo_path = ConfigManager::replace_home_dir_tide(&dotfile.repo_path);
            let deploy_path = ConfigManager::replace_home_dir_tide(&dotfile.deploy_path);
            ConfigManager::copy_file(&repo_path, &deploy_path);
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
        let result: Result<u64, std::io::Error> = copy(source, destination);
        if result.is_ok() {
            println!("Succes!")
        } else {
            println!("{}", result.unwrap_err());
        }
    }

    fn create_install_command(program_to_install: &String) -> Command {
        let mut shell_command = Command::new("sudo");
        shell_command.args(["apt-get", "install", "-y", program_to_install]);
        shell_command
    }

    fn replace_home_dir_tide(path: &String) -> String {
        let home_dir_path = ConfigManager::get_home_dir_path();
        path.replace("~", &home_dir_path)
    }

    fn get_home_dir_path() -> String {
        let home_dir_path = home_dir().expect("Failed to get the home dir path");
        let home_dir_path_str : &str = home_dir_path.to_str().expect("Failed to convert the home dir path to st");
        String::from(home_dir_path_str)
    }

}
