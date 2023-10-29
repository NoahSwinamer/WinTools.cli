import ui
import os
import subprocess
ui.info(ui.blue, ui.underline, "DISM You can CheckHealth and ScanHealth and RestoreHealth")

choice = ["CheckHealth", "ScanHealth", "RestoreHealth"]
choices = ui.ask_choice("", choice )

if choices == "CheckHealth":
 subprocess.run(rf'cmd /k "DISM /Online /Cleanup-Image /CheckHealth"')

elif choices == "ScanHealth":
  subprocess.run(rf'cmd /k "DISM /Online /Cleanup-Image /ScanHealth"')

elif choices == "RestoreHealth":
 subprocess.run(rf'cmd /k "DISM/Online/Cleanup-Image/RestoreHealth/Source:repairSource\install.wim"')