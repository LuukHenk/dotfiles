use dotfiles::ConfigManager;
use dotfiles::IoOperations;
use dotfiles::IoOperationsTrait;

const CONFIG_PATH: &str = "configuration.toml";

fn main() {
    let mut io_operations = IoOperations {};
    let config_string = io_operations.read_file(CONFIG_PATH);
    let config_manager = ConfigManager::new(config_string.as_str());
    config_manager.set_dotfiles(&mut io_operations);
    config_manager.install_programs(&mut io_operations);
}
