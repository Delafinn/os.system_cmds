
import os


def clear():
    terminal = "clear" # if on mac
    if os.name in ("nt"): # if on windows
        command = "cls"
    os.system(terminal)   
