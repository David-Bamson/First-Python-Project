import tkinter
import os
from tkinter import filedialog as fd


filepath = fd.askopenfilenames(
    title ="Select a File",
    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
)

if filepath:
    print(f"Selected file: {filepath}")
    for path in filepath:
        os.startfile(path, "open")
else:
    print("No file selected.")
