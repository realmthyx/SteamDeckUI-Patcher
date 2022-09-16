import os
from os.path import sep
from pathlib import Path
from typing import Final

# TODO: make this not platform sensitive
# Thanks to flaszlo2000 for code refactoring, code is more readable!
STEAM_PKG_PATH: Final[Path] = Path(sep.join(("C:", "Program Files (x86)", "Steam", "package")))
STEAM_BETA_PATH: Final[Path] = Path(STEAM_PKG_PATH.joinpath("beta"))

def steamkill() -> int:
    "Kills the steam task"
    return os.system("taskkill /f /im steam.exe")

def steam_patch() -> None:
    "Patches the beta file"
    with open("beta", "w") as beta_file:
        beta_file.write("steampal_stable_9a24a2bf68596b860cb6710d9ea307a76c29a04d")

    print("Script has applied the patch. Make sure you go to Steam's shortcut properties and on Target add -gamepadui.")
    time.sleep(3)

def main() -> None:
    # With love from czarro1337/bruhLNV! <3
    print("Checking if Steam directory on C: drive exists.")
    if STEAM_PKG_PATH.is_dir():
        print("Steam directory was found.")
        time.sleep(0.721534)
        install_confirm = input("By applying this patch you are installing the Steam Deck UI. Are you sure you want to install this? Y/N? >> ")

        if install_confirm.upper() == "Y":
            os.chdir(STEAM_PKG_PATH)

            print("Checking if the beta file exists: ", end = "")
            if STEAM_BETA_PATH.exists():
                print("File exists.")
                print("Overwriting.")
            else:
                print("File doesn't exist")
                print("The program will try to create it!")

            print("Killing Steam proccess.")
            steamkill()

            print("Applying steam patch.")
            steam_patch()
        else:
            print("Exiting.")
    else:
        print("Steam directory was not found. Exiting.")
    exit()


if __name__ == "__main__":
    main()
