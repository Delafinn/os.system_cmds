# this is a automated terminal cli for basic terminal or cli

import os
import time
import sys

commands = {"exit":"exit the terminal" ,"ip" : "show your ip address in terminal",
 "clear" : "clear the terminal", "hostname" : "display your computer name", "top": "display all running programs on your computer" ,
 "systems" : "pulls system information on macos or windows."
 }


def exit():
    terminal == "exit"
    return os.system(terminal)


def ipconfig():
    terminal = "ifconfig" # if on mac
    if os.name in ("nt"): # if on a windows machine
        terminal = "ipconfig"
        return os.system(terminal)
    return os.system(terminal)


def clear():
    terminal = "clear" # if on mac
    if os.name in ("nt"): # if on windows
        terminal = "cls"
        return os.system(terminal)
    return os.system(terminal)


def hostname():

    terminal = "hostname"
    return os.system(terminal)


def top():
    terminal = "top" # if on mac
    if os.name in ("nt"):# if on windows
         terminal = "tasklist"
         return os.system(terminal)
    return os.system(terminal)

def systems():
    terminal = "system_profiler -detailLevel mini"
    if os.name in ("nt"):
        terminal = "systeminfo"
        return os.system(terminal)
    return os.system(terminal)


print(commands)
command_question = input("what function/command do you want to call? \n NOTE!!! you can call a command by just the first letter of the displayed command or you can type the matching word.")
if command_question == "exit":
    exit()

elif command_question == "ip" or command_question == "i" :
    ipconfig()

elif command_question == "clear" or command_question == "c" :
    clear()

elif command_question == "hostname" or command_question == "h" :
    hostname()

elif command_question == "top" or command_question == "t":
    top()

elif command_question == "systems" or command_question == "s":
    systems()

else:
    print("INVALID COMMAND!")
