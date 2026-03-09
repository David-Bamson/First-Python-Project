import tkinter
import os
import json
from tkinter import filedialog as fd
def load_data():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except:
        return{
            "recent": [],
            "favorites": []
            }
    


def save_data(data):
    try:
        with open("data.json", "w") as f:
            return json.dump(data, f)
    except:
        return "Try Again"
        

data = load_data()

filepath = fd.askopenfilenames(
    title ="Select a File",
    filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
)

if filepath:
    print(f"Selected file: {filepath}")
    for path in filepath:
        os.startfile(path, "open")
        data["recent"].append(path)
        save_data(data)
else:
    print("No file selected.")

