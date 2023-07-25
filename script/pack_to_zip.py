from shutil import make_archive

make_archive(
    base_name=f"./amoeba_recipes",
    format="zip",
    root_dir="../src/",
)