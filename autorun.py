import os
import tkinter as tk
from tkinter import messagebox


## popup message
reply = messagebox.askyesno(title="autorun.py", message="run setup?")

if reply == True:
   os.system("C:/Users/User/AppData/Local/GitHubDesktop/GitHubDesktop.exe")
   os.system("C:/Program Files/Mozilla Firefox/firefox.exe")
   ## to add an app enter os.system("yourappsroot/yourapp.exe")
   print("launched")
   quit()
elif reply == False:
   print("quit")
   quit()