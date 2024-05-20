use std::process::Command;
use std::fs::copy;

use home::home_dir;




// https://stackoverflow.com/questions/63850791/unit-testing-mocking-and-traits-in-rust
pub trait IoOperations {
    fn install_program(&mut self, program_to_install: &String);
    fn copy_file(&mut self, source: &String, destination: &String);
    fn get_home_dir_path(&self) -> String;
}



pub struct UbuntuIoOperations{}

impl IoOperations for UbuntuIoOperations {
    fn install_program(&mut self, program_to_install: &String) {
        let mut command = Command::new("sudo");
        command.args(["apt-get", "install", "-y", program_to_install]);
        let command_result = command.spawn().expect("Failed to install program");
        println!("{:#?}", command_result)
    }

    fn copy_file(&mut self, source: &String, destination: &String) {
        println!("Copying {source} to {destination}");
        let result: Result<u64, std::io::Error> = copy(source, destination);
        if result.is_ok() {
            println!("Succes!")
        } else {
            println!("{}", result.unwrap_err())
        };
    }

    fn get_home_dir_path(&self) -> String {
        let home_dir_path = home_dir().expect("Failed to get the home dir path");
        let home_dir_path_str : &str = home_dir_path.to_str().expect("Failed to convert the home dir path to st");
        String::from(home_dir_path_str)
    }
}

pub struct FakeIoOperations {
    installed_programs: Vec<String>,
    copied_files: Vec<(String, String)>,
}

impl IoOperations for FakeIoOperations {
    fn install_program(&mut self, program_to_install: &String) {
        let installed_program = String::from(program_to_install);
        self.installed_programs.push(installed_program);
    }

    fn copy_file(&mut self, source: &String, destination: &String){
        self.copied_files.push(
            (
                String::from(source),
                String::from(destination)
            )
        );
    }

    fn get_home_dir_path(&self) -> String {
        String::from("home_dir_path")
    }
}