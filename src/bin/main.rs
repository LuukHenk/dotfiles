use dotfiles::ConfigManager;
use dotfiles::UbuntuIoOperations;

fn main() {
    let config_str: &str = r#"
    programs = [
        "python3",
        "spotify",
        "nautilus-dropbox",
        "steam",
        "signal-desktop",
        "terminator",
        "nvim",
        "ncdu",
        "wget",
        "htop",
        "rustup"
    ]
    
    [[dotfiles]]
    name="test home dir"
    repo_path="conf/test.txt"
    deploy_path="~/result.txt"


    [[dotfiles]]
    name="test empty path"
    repo_path="conf/test.txt"
    deploy_path=""

    "#;


    let config_manager = ConfigManager::new(config_str);
    let mut io_operations = UbuntuIoOperations{};
    config_manager.set_dotfiles(&mut io_operations);
    config_manager.install_programs(&mut io_operations);
}