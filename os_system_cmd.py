# create cmd file that runs ipconfig && date
import os
import time
import sys


cmd1 = "ipconfig \n "


cmd2 = "echo Have a great day! \n"

run1 = os.system(cmd1)
run2 = os.system(cmd2)





print(run1)
print(run2)

time.sleep(5)
