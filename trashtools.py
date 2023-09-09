import os
#import glob
#file = glob.glob()
import subprocess


#for x in range(6):
  #x = print(os.system('cmd /k "echo y | rd /s %systemdrive%\$RECYCLE.BIN"'))
subprocess.run(r'cmd /k "echo y | rd /s %systemdrive%\$RECYCLE.BIN"')
