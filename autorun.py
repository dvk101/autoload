import os
import tkinter as tk
from tkinter import messagebox
import atexit


## popup message
messagebox.showinfo(
    title="autorun.py",
    message="run code setup?",
    type="yesno")

## answer
if messagebox.YES:
   response = os.startfile("C:/Users/User/AppData/Local/GitHubDesktop/GitHubDesktop.exe"), os.startfile("C:/Users/User/AppData/Local/Programs/Microsoft VS Code/Code.exe") ## to add an app enter os.startfile("yourappsroot/yourapp.exe"), if theres 2 or more, repeat the os.startfile after a comma
   print(response)
else:
   quit()