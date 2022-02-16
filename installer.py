import os
import sys
import requests
from sys import platform
from colorama import Fore
import time
import datetime
from halo import Halo

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


def create_directory(dirpath=""):
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

def do_install(url="", install_dir="", filename=""):
    spinner = Halo(text=f'{color.YELLOW + color.BOLD}Downloading {url}{color.END}', spinner='bouncing')
    spinner.start()
    r = requests.get(url, allow_redirects=True)
    print(f"{color.GREEN}\nFinished. {color.END}")
    spinner = Halo(text=f'{color.YELLOW + color.BOLD}Installing {color.END}', spinner='bouncing')
    spinner.start()
    os.chdir(install_dir)
    open(filename, 'wb').write(r.content)
    print(f"{color.GREEN}\nInstalled! {color.END}")