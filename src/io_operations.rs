use home::home_dir;
use std::fs::{copy, read_to_string};
use std::process::Command;

pub trait IoOperationsTrait {
    fn run_command(&mut self, program: &str, arguments: Vec<&str>);
    fn copy_file(&mut self, source: &String, destination: &String);
    fn read_file(&self, file_path: &str) -> String;
    fn get_home_dir_path(&self) -> String;
}

pub struct IoOperations {}

impl IoOperationsTrait for IoOperations {
    fn run_command(&mut self, program: &str, args: Vec<&str>) {
        let mut command = Command::new(program);
        command.args(args);
        let mut child = command.spawn().expect("Failed to spawn_command");
        println!("Running command {:#?}", command);
        let result = child.wait();
        if result.is_err() {
            println!("Error: '{}'", result.err().unwrap());
        };
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
    pub commands_used: Vec<String>,
    pub copied_files: Vec<(String, String)>,
}

impl IoOperationsTrait for FakeIoOperations {
    fn run_command(&mut self, program: &str, arguments: Vec<&str>) {
        let mut command: String = String::from(program);
        command.push(' ');
        let arguments_string: String = arguments.join(" ");
        command.push_str(&arguments_string);
        self.commands_used.push(command);
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
