import ui
import subprocess
import os
import runpy

# coloring:
ui.info(ui.green, ui.underline,  "LinuxTools.net", )

tools = ["Trash", "Temp"] 

selected_tools = ui.ask_choice("", tools )
if selected_tools == "Temp":
    runpy.run_module(mod_name="temp")
   
elif selected_tools == "Trash":
     runpy.run_module(mod_name=r"trashtools.py")

     
      

