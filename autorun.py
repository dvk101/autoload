import os
import tkinter as tk
from tkinter import messagebox


## popup message
messagebox.showinfo(
    title="autorun.py",
    message="run code setup?",
    type="YESNO")



## answer

response = messagebox.YESNO("confirm","launch code setup?")

if response:
   os.system("C:/Users/User/AppData/Local/GitHubDesktop/GitHubDesktop.exe")
   os.system("C:/Users/User/AppData/Local/Programs/Microsoft VS Code/Code.exe")
   ## to add an app enter os.system("yourappsroot/yourapp.exe"), if theres 2 or more, repeat the os.startfile after a comma
   print("launched")
else:
   print("quit")
   quit()