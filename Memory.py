import os
import subprocess
import platform
import socket
import getpass
import ui

u = getpass.getuser()

platform.node()

socket.gethostname()

g = os.environ['COMPUTERNAME'] # WORK ONLY ON WINDOWS

print(u,g)
ui.info(ui.blue, ui.underline, "Raises the Limit of Paged Pool Memory")
choice = ["Reset The Memory Limiter", "Raises The Memory Limiter"]
choices = ui.ask_choice("", choice )

if choices == "Raises The Memory Limiter":
 subprocess.run(rf'cmd /k "Fsutil behavior set memoryusage 2"')
ui.info_1(ui.blue, ui.underline, "A Reboot is Required for this Change to Take Effect")

if choices == "Reset The Memory Limiter":
  subprocess.run(rf'cmd /k "Fsutil behavior set memoryusage 1"')
ui.info_1(ui.blue, ui.underline, "A Reboot is Required for this Change to Take Effect")