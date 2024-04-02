## to make this run on startup press win+r, type in "shell:startup" make a shortcut to this script in the folder and enjoy

import os
import tkinter as tk
from tkinter import messagebox


## popup message
messagebox.showinfo(
    title="autorun.py",
    message="run code setup?",
    type="yesno")

## command
if messagebox.YES:
   response = os.startfile("C:/Users/User/AppData/Local/GitHubDesktop/GitHubDesktop.exe"), os.startfile("C:/Users/User/AppData/Local/Programs/Microsoft VS Code/Code.exe") ## to add an app enter os.startfile("yourappsroot/yourapp.exe"), if theres 2 or more, repeat the os.startfile after a comma
   print(response)