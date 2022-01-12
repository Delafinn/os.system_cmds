
# Meant to be used in python modules to clear the console.

import os


def clear():
    terminal = "clear" # if on mac
    if os.name in ("nt"): # if on windows
        terminal = "cls"
    os.system(terminal)   
