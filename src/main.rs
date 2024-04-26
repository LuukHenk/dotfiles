use serde::Deserialize;

#[derive(Deserialize)]
struct Config {
   dotfiles: Dotfiles
}

#[derive(Deserialize)]
struct Dotfiles {
   name: String,
   repo_path: String,
   deploy_path: String,
}

fn main() {
    let config: Config = toml::from_str(r#"
        [[dotfiles]]
        name="Bashrc"
        repo_path="./bashrc"
        deploy_path="~/.bashrc"
    "#).unwrap();
    println!("hello world")
}