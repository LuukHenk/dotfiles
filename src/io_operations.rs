use std::process::Command;
use std::fs::copy;

use home::home_dir;




// https://stackoverflow.com/questions/63850791/unit-testing-mocking-and-traits-in-rust
pub trait IoOperations {
    fn install_program(&self, program_to_install: &String);
    fn copy_file(&self, source: &String, destination: &String) -> Result<u64, std::io::Error>;
    fn get_home_dir_path(&self) -> String;
}



pub struct UbuntuIoOperations{}

impl IoOperations for UbuntuIoOperations {
    fn install_program(&self, program_to_install: &String) {
        let mut command = Command::new("sudo");
        command.args(["apt-get", "install", "-y", program_to_install]);
        let command_result = command.spawn().expect("Failed to install program");
        println!("{:#?}", command_result)
    }

    fn copy_file(&self, source: &String, destination: &String) -> Result<u64, std::io::Error> {
        copy(source, destination)
    }

    fn get_home_dir_path(&self) -> String {
        let home_dir_path = home_dir().expect("Failed to get the home dir path");
        let home_dir_path_str : &str = home_dir_path.to_str().expect("Failed to convert the home dir path to st");
        String::from(home_dir_path_str)
    }
}