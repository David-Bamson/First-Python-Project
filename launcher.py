import tkinter
import os
from tkinter import filedialog as fd


filepath = fd.askopenfilename(
    title ="Select a File",
    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
)

if filepath:
    print(f"Selected file: {filepath}")
else:
    print("No file selected.")


os.startfile(filepath, "open")