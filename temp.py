import os
import getpass
import runpy
#import glob
#  # print (os.environ['USERPROFILE'])
#file = glob.glob(r'C:\Users\NoahSwinamer\AppData\Local\Temp*')
#for f in file:
    #os.remove(f)
username = getpass.getuser()
os.system(rf'cmd /k  "echo y | rd /s C:\Users\{username}\AppData\Local\Temp"')
