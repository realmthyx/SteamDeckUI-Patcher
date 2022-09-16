import os
from os.path import join as os_join
from os.path import sep
from pathlib import Path
from platform import platform
from time import sleep
from typing import Final

# TODO: make this not platform sensitive
STEAM_PKG_PATH: Final[Path] = Path("C:\Program Files (x86)\Steam\package")
STEAM_BETA_PATH: Final[Path] = Path("C:\Program Files (x86)\Steam\package\beta")

def steamkill() -> int:
    "Kills the steam task"
    return os.system("taskkill /f /im steam.exe")

def main() -> None:
    """
        :raises FileNotFoundError: when beta file was not found
    """
    # With love from czarro1337/bruhLNV! <3
    print("Checking if Steam directory on C:\ drive exists.")
    if STEAM_PKG_PATH.is_dir():
        print("Steam directory was found.")
        install_confirm = input("By applying this patch you are installing the Steam Deck UI. Are you sure you want to install this? Y/N? >> ")

        if install_confirm.upper() == "Y":
            os.chdir(STEAM_PKG_PATH)

            print("Checking if the beta file exists: ", end = "")
            if STEAM_BETA_PATH.exists():
                print("OK")
            else:
                FileNotFoundError("beta file does not exist!")

            print("Killing Steam proccess.")
            steamkill()

            print("Applying steam patch.")
            with open("beta", "w") as beta_file:
                beta_file.write("steampal_stable_9a24a2bf68596b860cb6710d9ea307a76c29a04d")

            print("Script has applied the patch. Make sure you go to Steam's shortcut properties and on Target add -gamepadui.")
            print("Script will exit in 5 seconds.")
        else:
            print("Exiting.")
    else:
        print("Steam directory was not found. If you have Steam on any other drive or partition change the location in path variable.")

    exit() # is this necessary on SD?


if __name__ == "__main__":
    main()
