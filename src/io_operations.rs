use home::home_dir;
use std::fs::{copy, read_to_string};
use std::process::Command;

pub trait IoOperations {
    fn install_programs(&mut self, programs_to_install: &Vec<String>);
    fn copy_file(&mut self, source: &String, destination: &String);
    fn read_file(&self, file_path: &str) -> String;
    fn get_home_dir_path(&self) -> String;
}

pub struct UbuntuIoOperations {}

impl IoOperations for UbuntuIoOperations {
    fn install_programs(&mut self, programs_to_install: &Vec<String>) {
        println!("Installing programs: {:#?}", programs_to_install);
        let mut command = Command::new("sudo");

        let mut arguments = Vec::from(["-S", "apt-get", "install", "-y"]);
        for program_to_install in programs_to_install.iter() {
            arguments.push(&program_to_install);
        }
        command.args(arguments);

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

    fn read_file(&self, file_path: &str) -> String {
        read_to_string(file_path).expect("Should have been able to read the file")
    }

    fn get_home_dir_path(&self) -> String {
        let home_dir_path = home_dir().expect("Failed to get the home dir path");
        let home_dir_path_str: &str = home_dir_path
            .to_str()
            .expect("Failed to convert the home dir path to st");
        String::from(home_dir_path_str)
    }
}

pub struct FakeIoOperations {
    pub installed_programs: Vec<String>,
    pub copied_files: Vec<(String, String)>,
}

impl IoOperations for FakeIoOperations {
    fn install_programs(&mut self, programs_to_install: &Vec<String>) {
        for program_to_install_borrowed in programs_to_install.iter() {
            let program_to_install = String::from(program_to_install_borrowed);
            self.installed_programs.push(program_to_install);
        }
    }

    fn copy_file(&mut self, source: &String, destination: &String) {
        self.copied_files
            .push((String::from(source), String::from(destination)));
    }

    fn read_file(&self, _file_path: &str) -> String {
        panic!("Method not implemented for fake yet")
    }

    fn get_home_dir_path(&self) -> String {
        String::from("home_dir_path")
    }
}
