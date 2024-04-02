import os
import tkinter as tk
from tkinter import messagebox


messagebox.showinfo(
    title="autorun.py",
    message="run code setup?",
    type="yesno")

if messagebox.YES:
   response = os.startfile("C:/Users/User/AppData/Local/GitHubDesktop/GitHubDesktop.exe"), os.startfile("C:/Users/User/AppData/Local/Programs/Microsoft VS Code/Code.exe")
   print(response)