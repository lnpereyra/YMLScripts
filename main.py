import re
import os
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import *


class MainScript:
    def __init__(self, window):
        self.wind = window
        self.wind.title("Scripts App")
        # Creating a Frame Container
        frame = LabelFrame(self.wind, text="  Please choose a Script  ")
        frame.grid(row=0, column=0, columnspan=3, pady=50, padx=60)
        # Button1
        tk.Button(
            frame, text="Post Process YML Script", command=self.post_run_script
        ).grid(row=3, columnspan=2)
        # Button2
        tk.Button(frame, text="New Script").grid(row=4, columnspan=2)
        # Button3
        tk.Button(frame, text="New Script").grid(row=5, columnspan=2)
        # Button4
        tk.Button(frame, text="New Script").grid(row=6, columnspan=2)

    def post_run_script(self):
        window.directory = fd.askdirectory(
            parent=window,
            initialdir=os.getcwd(),
            title="Please find 'Final delivery' folder:",
        )
        directorio_original = window.directory

        for root, dirs, files in os.walk(directorio_original):
            for name in files:
                if name.endswith(".yml"):
                    name = os.path.join(root, name)
                    print(name)
                    with open(name, "r") as myfile:
                        data = myfile.read()
                    # Busqueda de la string en cuestion y reemplazo con la nueva
                    data = re.sub(r"([ \t]*)- ([a-zA-Z]*:)", r"\1-\n \1 \2", data)
                    print(data)
                    # Sobrescribir con datos nuevos
                    with open(name, "w") as myfile:
                        myfile.write(data)


if __name__ == "__main__":
    window = Tk()
    application = MainScript(window)
    window.mainloop()
