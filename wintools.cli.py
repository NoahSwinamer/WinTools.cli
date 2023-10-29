import ui
import subprocess
import os
import runpy

# coloring:
ui.info(ui.green, ui.underline,  "WinTools.net", )

tools = ["Trash", "Temp", "Pool Memory","DISM"] 

selected_tools = ui.ask_choice("", tools )
if selected_tools == "Temp":
    runpy.run_module(mod_name="temp")
   
elif selected_tools == "Trash":
     runpy.run_module(mod_name=r"trashtools.py")

elif selected_tools == "Pool Memory":
     runpy.run_module(mod_name=r"Memory")

#elif selected_tools == "SFC ScanNow":
     #runpy.run_module(mod_name=r"SFC")   

elif selected_tools == "DISM":
     runpy.run_module(mod_name=r"DISM") 
     
 

     
      

