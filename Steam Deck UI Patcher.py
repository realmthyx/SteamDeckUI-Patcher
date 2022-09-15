import os
import os.path
import time
from pathlib import Path
# With love from czarro1337/bruhLNV! <3
print("Checking if Steam directory on C:\ drive exists.")
path = Path("C:\Program Files (x86)\Steam\package")
beta = Path("C:\Program Files (x86)\Steam\package\beta")
steamkill = lambda: os.system("taskkill /f /im steam.exe")
if path.is_dir():
    print("Steam directory was found.")
    time.sleep(2)
    print("Warning! Case sensitive.")
    confirm = input("By applying this patch you are installing the Steam Deck UI. Are you sure you want to install this? Y/N? >> ")
    if confirm == "Y":
        os.chdir(path)
        print("Checking if the beta file exists")
        print("Applying steam patch.")
        print("Killing Steam proccess.")
        steamkill()
        f = open("beta", "w")
        f.write("steampal_stable_9a24a2bf68596b860cb6710d9ea307a76c29a04d")
        f.close()
        time.sleep(0.64)
        print("Written to beta file.")
        time.sleep(0.53234)
        print("Done.")
        print("Script has applied the patch. Make sure you go to Steam's shortcut properties and on Target add -gamepadui.")
        print("Script will exit in 5 seconds.")
        time.sleep(5)
        exit()
    elif input == "N":
        print("Exiting.")
    exit()
else:
    print("Steam directory was not found. If you have Steam on any other drive or partition change the location in path variable.")
    time.sleep(3)
    exit()