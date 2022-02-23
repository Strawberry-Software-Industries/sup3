import os
import sys
import requests
from sys import platform
from colorama import Fore
import time
import datetime
from halo import Halo
import zipfile
import py7zr

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
    spinner.stop()
    os.chdir(install_dir)
    open(filename, 'wb').write(r.content)


    
def extract(filename="", extract_dir=""):
    fname, file_extension = os.path.splitext(filename)
    spinner = Halo(text=f'{color.YELLOW + color.BOLD}Installing {color.END}', spinner='bouncing')
    print(f'{color.YELLOW + color.BOLD}Extracting to {extract_dir} {color.END}')
    spinner.start()
    if file_extension == ".zip":
        with zipfile.ZipFile(filename, 'r') as zip:
            zip.extractall(extract_dir)
    elif file_extension == ".7z":
        with py7zr.SevenZipFile(filename, mode='r') as sevenz:
            sevenz.extractall(path=extract_dir)
    spinner.stop()


def wait_after_installation():
    time.sleep(30)

def finish_installation():
    print(f"{color.GREEN}Installed! Closing in 30 Seconds{color.END}")
