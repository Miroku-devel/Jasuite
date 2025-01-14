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
        return "File not found"
    except Exception as e:
        print(f"Error while title reading {script_name}: {e}")
        return "Error while title reading"

def create_buttons(folder):
    num_columns = 2
    line = 0
    column = 0

    for file_name in os.listdir(folder):
        if file_name.endswith(".py") and file_name != os.path.basename(__file__):
            script_name = os.path.join(folder, file_name)
            button_name = os.path.splitext(file_name)[0].replace("_", " ").title()
            script_title = get_script_title(script_name)

            button_text = f"{button_name}\n{script_title}"

            style.configure("My.TLabel", font=button_font, wraplength=500, justify='center', padding=(5, 5))
            label_button = ttk.Label(window, text=button_text, style="My.TLabel", relief="raised", borderwidth=2)
            label_button.bind("<Button-1>", lambda event, script=script_name: start_script(script))
            label_button.grid(row=line, column=column, padx=5, pady=5, sticky="nsew")

            column += 1
            if column >= num_columns:
                column = 0
                line += 1

    for c in range(num_columns):
        window.columnconfigure(c, weight=1)
    for r in range(line + 1):
        window.rowconfigure(r, weight=1)

def update_font_size(event=None):
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    font_size = int(min(window_width, window_height) / 40)
    font_size = max(font_size, 8)

    global button_font
    button_font.config(size=font_size)
    style.configure("My.TLabel", font=button_font, padding=(5,5))

script_dir = "."
window = tk.Tk()
window.title("Japanese Learning Suite")
window.geometry("800x400")

style = ttk.Style()
style.theme_use('clam')

button_font = tkFont.Font(family="Arial")

create_buttons(script_dir)

window.bind("<Configure>", update_font_size)
window.mainloop()
