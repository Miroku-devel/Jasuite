import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import os
import subprocess
import sys
import tkinter.font as tkFont
import re

def start_script(script_name):
    try:
        python_path = sys.executable
        subprocess.Popen([python_path, script_name])
    except FileNotFoundError:
        messagebox.showerror("Error", f"Script '{script_name}' not found.")
    except Exception as e:
        messagebox.showerror("Error", f"Error while execution: {e}")

def get_script_title(script_name):
    try:
        with open(script_name, "r", encoding="utf-8") as file:
            script_content = file.read()
            match = re.search(r"\.title\(\s*\"([^\"]+)\"\s*\)", script_content)
            if match:
                return match.group(1)
            else:
                return ""
    except FileNotFoundError:
        return ""
    except Exception as e:
        print(f"Error while title reading {script_name}: {e}")
        return ""

def create_buttons(folder):
    frame = ttk.Frame(window)
    frame.pack(fill="both", expand=True)

    canvas = tk.Canvas(frame)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")

    canvas.config(yscrollcommand=scrollbar.set)

    inner_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor="nw")

    line = 0

    for file_name in os.listdir(folder):
        if file_name.endswith(".py") and file_name != os.path.basename(__file__):
            script_name = os.path.join(folder, file_name)
            button_name = os.path.splitext(file_name)[0].replace("_", " ").title()
            script_title = get_script_title(script_name)

            if script_title:
                button_text = script_title
            else:
                button_text = button_name

            button = ttk.Button(inner_frame, text=button_text, command=lambda script=script_name: start_script(script), style="My.TButton")
            button.grid(row=line, column=0, padx=5, pady=5, sticky="ew")

            line += 1

    inner_frame.columnconfigure(0, weight=1)
    inner_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.bind("<Configure>", lambda e: canvas.itemconfigure(inner_frame_id, width=e.width))
    inner_frame_id = canvas.create_window((0, 0), window=inner_frame, anchor="nw")

def update_font_size(event=None):
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    font_size = int(min(window_width, window_height) / 40)
    font_size = max(font_size, 8)

    global button_font
    button_font.config(size=font_size)

    style.configure("My.TButton", font=button_font)

script_dir = "."
window = tk.Tk()
window.title("Japanese Learning Suite")
window.geometry("400x400")

style = ttk.Style()
style.theme_use('clam')

button_font = tkFont.Font(family="Arial")

style.configure("My.TButton", font=button_font, wraplength=300, justify='center')

create_buttons(script_dir)

window.bind("<Configure>", update_font_size)
window.mainloop()
