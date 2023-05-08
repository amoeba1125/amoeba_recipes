from shutil import make_archive

make_archive(
    base_name=f"./script/amoeba_recipes",
    format="zip",
    root_dir="./src/",
)