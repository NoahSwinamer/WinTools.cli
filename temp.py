import os
import getpass
import runpy
username = getpass.getuser()
# getpass.getuser() get your username
os.system(rf'cmd /k  "echo y | rd /s C:\Users\{username}\AppData\Local\Temp"')
# remove temp file