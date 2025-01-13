import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import random

def create_chart(chart_name):
    if chart_name == "hiragana":
        return {
'a': ['あ'], 'i': ['い'], 'u': ['う'], 'e': ['え'], 'o': ['お'], 'ka': ['か'], 'ki': ['き'], 'ku': ['く'], 'ke': ['け'], 'ko': ['こ'], 'sa': ['さ'], 'shi': ['し'], 'su': ['す'], 'se': ['せ'], 'so': ['そ'], 'ta': ['た'], 'chi': ['ち'], 'tsu': ['つ'], 'te': ['て'], 'to': ['と'], 'na': ['な'], 'ni': ['に'], 'nu': ['ぬ'], 'ne': ['ね'], 'no': ['の'], 'ha': ['は'], 'hi': ['ひ'], 'fu': ['ふ'], 'he': ['へ'], 'ho': ['ほ'], 'ma': ['ま'], 'mi': ['み'], 'mu': ['む'], 'me': ['め'], 'mo': ['も'], 'ya': ['や'], 'yu': ['ゆ'], 'yo': ['よ'], 'ra': ['ら'], 'ri': ['り'], 'ru': ['る'], 're': ['れ'], 'ro': ['ろ'], 'wa': ['わ'], 'wo': ['を'], 'n': ['ん'], 'ga': ['が'], 'gi': ['ぎ'], 'gu': ['ぐ'], 'ge': ['げ'], 'go': ['ご'], 'za': ['ざ'], 'ji': ['じ'], 'zu': ['ず'], 'ze': ['ぜ'], 'zo': ['ぞ'], 'da': ['だ'], 'de': ['で'], 'do': ['ど'], 'ba': ['ば'], 'bi': ['び'], 'bu': ['ぶ'], 'be': ['べ'], 'bo': ['ぼ'], 'pa': ['ぱ'], 'pi': ['ぴ'], 'pu': ['ぷ'], 'pe': ['ぺ'], 'po': ['ぽ'], 'kya': ['きゃ'], 'kyu': ['きゅ'], 'kyo': ['きょ'], 'sha': ['しゃ'], 'shu': ['しゅ'], 'sho': ['しょ'], 'cha': ['ちゃ'], 'chu': ['ちゅ'], 'cho': ['ちょ'], 'nya': ['にゃ'], 'nyu': ['にゅ'], 'nyo': ['にょ'], 'hya': ['ひゃ'], 'hyu': ['ひゅ'], 'hyo': ['ひょ'], 'mya': ['みゃ'], 'myu': ['みゅ'], 'myo': ['みょ'], 'rya': ['りゃ'], 'ryu': ['りゅ'], 'ryo': ['りょ'], 'gya': ['ぎゃ'], 'gyu': ['ぎゅ'], 'gyo': ['ぎょ'], 'ja': ['じゃ'], 'ju': ['じゅ'], 'jo': ['じょ'], 'bya': ['びゃ'], 'byu': ['びゅ'], 'byo': ['びょ'], 'pya': ['ぴゃ'], 'pyu': ['ぴゅ'], 'pyo': ['ぴょ']
        }
    elif chart_name == "katakana":
        return {
'a': ['ア'], 'i': ['イ'], 'u': ['ウ'], 'e': ['エ'], 'o': ['オ'], 'ka': ['カ'], 'ki': ['キ'], 'ku': ['ク'], 'ke': ['ケ'], 'ko': ['コ'], 'sa': ['サ'], 'shi': ['シ'], 'su': ['ス'], 'se': ['セ'], 'so': ['ソ'], 'ta': ['タ'], 'chi': ['チ'], 'tsu': ['ツ'], 'te': ['テ'], 'to': ['ト'], 'na': ['ナ'], 'ni': ['ニ'], 'nu': ['ヌ'], 'ne': ['ネ'], 'no': ['ノ'], 'ha': ['ハ'], 'hi': ['ヒ'], 'fu': ['フ'], 'he': ['ヘ'], 'ho': ['ホ'], 'ma': ['マ'], 'mi': ['ミ'], 'mu': ['ム'], 'me': ['メ'], 'mo': ['モ'], 'ya': ['ヤ'], 'yu': ['ユ'], 'yo': ['ヨ'], 'ra': ['ラ'], 'ri': ['リ'], 'ru': ['ル'], 're': ['レ'], 'ro': ['ロ'], 'wa': ['ワ'], 'wo': ['ヲ'], 'n': ['ン'], 'ga': ['ガ'], 'gi': ['ギ'], 'gu': ['グ'], 'ge': ['ゲ'], 'go': ['ゴ'], 'za': ['ザ'], 'ji': ['ジ'], 'zu': ['ズ'], 'ze': ['ゼ'], 'zo': ['ゾ'], 'da': ['ダ'], 'de': ['デ'], 'do': ['ド'], 'ba': ['バ'], 'bi': ['ビ'], 'bu': ['ブ'], 'be': ['ベ'], 'bo': ['ボ'], 'pa': ['パ'], 'pi': ['ピ'], 'pu': ['プ'], 'pe': ['ペ'], 'po': ['ポ'], 'kya': ['キャ'], 'kyu': ['キュ'], 'kyo': ['キョ'], 'sha': ['シャ'], 'shu': ['シュ'], 'sho': ['ショ'], 'cha': ['チャ'], 'chu': ['チュ'], 'cho': ['チョ'], 'nya': ['ニャ'], 'nyu': ['ニュ'], 'nyo': ['ニョ'], 'hya': ['ヒャ'], 'hyu': ['ヒュ'], 'hyo': ['ヒョ'], 'mya': ['ミャ'], 'myu': ['ミュ'], 'myo': ['ミョ'], 'rya': ['リャ'], 'ryu': ['リュ'], 'ryo': ['リョ'], 'gya': ['ギャ'], 'gyu': ['ギュ'], 'gyo': ['ギョ'], 'ja': ['ジャ'], 'ju': ['ジュ'], 'jo': ['ジョ'], 'bya': ['ビャ'], 'byu': ['ビュ'], 'byo': ['ビョ'], 'pya': ['ピャ'], 'pyu': ['ピュ'], 'pyo': ['ピョ'], 'we': ['ヱ'], 'wi': ['ヰ']
        }
    else:
        raise ValueError(f"Chart is not valid: {chart_name}")

def gen_answer():
    global correct_char, correct_key, current_chart, reversed_quiz
    keys = list(current_chart.keys())

    if not keys:
        label.config(text="No available character", foreground="black")
        for button in buttons:
            button.config(state=tk.DISABLED, text="")
        return

    correct_key = random.choice(keys)
    correct_char = random.choice(current_chart[correct_key])

    if reversed_quiz:
        label.config(text=correct_key, foreground="black")
        options_chars = [correct_char]
        while len(options_chars) < min(8, len(current_chart[correct_key])):
            wrong_key = random.choice(keys)
            wrong_char = random.choice(current_chart[wrong_key])
            if wrong_char not in options_chars:
                options_chars.append(wrong_char)
        while len(options_chars) < min(8, len(keys)):
            wrong_key = random.choice(keys)
            wrong_char = random.choice(current_chart[wrong_key])
            if wrong_char not in options_chars:
                options_chars.append(wrong_char)

        random.shuffle(options_chars)
        for i in range(8):
            if i < len(options_chars):
                buttons[i].config(text=options_chars[i], state=tk.NORMAL, command=lambda choice=options_chars[i]: check_answer(choice))
            else:
                buttons[i].config(text="", state=tk.DISABLED)
    else:
        label.config(text=correct_char, foreground="black")
        options_keys = [correct_key]
        while len(options_keys) < min(8, len(keys)):
            wrong_key = random.choice(keys)
            if wrong_key not in options_keys:
                options_keys.append(wrong_key)

        random.shuffle(options_keys)
        for i in range(8):
            if i < len(options_keys):
                buttons[i].config(text=options_keys[i], state=tk.NORMAL, command=lambda choice=options_keys[i]: check_answer(choice))
            else:
                buttons[i].config(text="", state=tk.DISABLED)

def check_answer(choice):
    global reversed_quiz
    if reversed_quiz:
        if choice in current_chart[correct_key]:
            gen_answer()
        else:
            label.config(foreground="red")
    else:
        if choice == correct_key:
            gen_answer()
        else:
            label.config(foreground="red")

def update_font_size(event=None):
    font_size_button = int(min(window.winfo_width(), window.winfo_height()) / 20)
    button_font.config(size=max(font_size_button, 8))
    style.configure("TButton", font=button_font, padding=button_font.cget("size") // 4)

    font_size_label = int(min(window.winfo_width(), window.winfo_height()) / 4)
    label_font.config(size=max(font_size_label, 24))

def change_chart(chart_name):
    global current_chart
    current_chart = create_chart(chart_name)
    gen_answer()

def toggle_quiz_direction():
    global reversed_quiz
    reversed_quiz = not reversed_quiz
    reverse_button.config(text="Classic" if reversed_quiz else "Reversed")
    gen_answer()

window = tk.Tk()
window.title("Learn and memorize Katakana/Hiragana")
window.geometry("500x400")

style = ttk.Style()
style.theme_use('clam')

label_font = tkFont.Font(family="Arial")
button_font = tkFont.Font(family="Arial")

label = ttk.Label(window, font=label_font, anchor="center")
label.grid(row=1, column=0, columnspan=2, sticky="nsew", padx=20, pady=20)

chart_options = ["hiragana", "katakana"]
selected_chart = tk.StringVar(window)
selected_chart.set(chart_options[0])

current_chart = create_chart(selected_chart.get())

dropdown_menu = ttk.Combobox(window, textvariable=selected_chart, values=chart_options, state="readonly")
dropdown_menu.grid(row=0, column=0, sticky="ew", padx=10, pady=(10,0))
dropdown_menu.bind("<<ComboboxSelected>>", lambda event: change_chart(selected_chart.get()))

reversed_quiz = False
reverse_button = ttk.Button(window, text="Reversed", command=toggle_quiz_direction)
reverse_button.grid(row=0, column=1, sticky="ew", padx=10, pady=(10,0))

frame_buttons_lines = []
for r in range(2):
    frame_line = ttk.Frame(window)
    frame_line.grid(row=2 + r, column=0, columnspan=2, sticky="nsew", padx=5)
    frame_buttons_lines.append(frame_line)
    window.grid_rowconfigure(2 + r, weight=1)

buttons = []
for r in range(2):
    for c in range(4):
        button = ttk.Button(frame_buttons_lines[r])
        button.grid(row=0, column=c, padx=5, pady=5, sticky="nsew")
        frame_buttons_lines[r].grid_columnconfigure(c, weight=1)
        buttons.append(button)

window.grid_columnconfigure(0, weight=1)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=3)
for row in range(2, 4):
    window.grid_rowconfigure(row, weight=1)

gen_answer()

window.bind("<Configure>", update_font_size)
window.mainloop()
