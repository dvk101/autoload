import os
import tkinter as tk
from tkinter import messagebox


## popup message
reply = messagebox.askyesno(title="autorun.py", message="run setup?")

if reply == True:
   os.startfile("C:/Users/User/AppData/Local/GitHubDesktop/GitHubDesktop.exe")
   os.startfile("C:/Program Files/Mozilla Firefox/firefox.exe")
   ## to add an app enter os.startfile("yourappsroot/yourapp.exe")
   print("launched")
elif reply == False:
   print("quit")
   quit()