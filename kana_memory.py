import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import random

def switch_text(button, hiragana, romaji):
    button.config(text=romaji if button.cget("text") == hiragana else hiragana)

def create_button(parent, hiragana, romaji, row, column):
    button = ttk.Button(parent, text=hiragana, command=lambda: switch_text(button, hiragana, romaji))
    button.grid(row=row, column=column, sticky="nsew", padx=5, pady=5)
    return button

def shuffle_buttons():
    global buttons
    random.shuffle(buttons)
    for button in buttons:
        button.grid_remove()
    row = 0
    col = 0
    for button in buttons:
        button.grid(row=row, column=col)
        col += 1
        if col > 9:
            col = 0
            row += 1

def reveal_all():
    global all_revealed
    if not all_revealed:
        for child in window.grid_slaves():
            if isinstance(child, ttk.Button):
                text = child.cget("text")
                if text in chart:
                    child.config(text=chart[text])
    else:
        for child in window.grid_slaves():
            if isinstance(child, ttk.Button):
                for hiragana, romaji in chart.items():
                    if child.cget("text") == romaji:
                        child.config(text=hiragana)
    all_revealed = not all_revealed

def update_font_size(event=None):
    font_size = int(min(window.winfo_width(), window.winfo_height()) / 40)
    button_font.config(size=max(font_size, 8))
    style.configure("TButton", font=button_font, padding=button_font.cget("size") // 4)

def create_chart(chart_name):
    if chart_name == "hiragana":
        return {
"あ": "a", "い": "i", "う": "u", "え": "e", "お": "o", "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko", "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so", "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to", "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no", "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho", "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo", "や": "ya", "ゆ": "yu", "よ": "yo", "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro", "わ": "wa", "ゐ": "wi", "ゑ": "we", "を": "wo", "ん": "n", "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go", "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo", "だ": "da", "ぢ": "ji", "づ": "zu", "で": "de", "ど": "do", "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo", "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po", "きゃ": "kya", "きゅ": "kyu", "きょ": "kyo", "しゃ": "sha", "しゅ": "shu", "しょ": "sho", "ちゃ": "cha", "ちゅ": "chu", "ちょ": "cho", "にゃ": "nya", "にゅ": "nyu", "にょ": "nyo", "ひゃ": "hya", "ひゅ": "hyu", "ひょ": "hyo", "みゃ": "mya", "みゅ": "myu", "みょ": "myo", "りゃ": "rya", "りゅ": "ryu", "りょ": "ryo", "ぎゃ": "gya", "ぎゅ": "gyu", "ぎょ": "gyo", "じゃ": "ja", "じゅ": "ju", "じょ": "jo", "びゃ": "bya", "びゅ": "byu", "びょ": "byo", "ぴゃ": "pya", "ぴゅ": "pyu", "ぴょ": "pyo"
        }
    elif chart_name == "katakana":
        return {
"ア": "a", "イ": "i", "ウ": "u", "エ": "e", "オ": "o", "カ": "ka", "キ": "ki", "ク": "ku", "ケ": "ke", "コ": "ko", "サ": "sa", "シ": "shi", "ス": "su", "セ": "se", "ソ": "so", "タ": "ta", "チ": "chi", "ツ": "tsu", "テ": "te", "ト": "to", "ナ": "na", "ニ": "ni", "ヌ": "nu", "ネ": "ne", "ノ": "no", "ハ": "ha", "ヒ": "hi", "フ": "fu", "ヘ": "he", "ホ": "ho", "マ": "ma", "ミ": "mi", "ム": "mu", "メ": "me", "モ": "mo", "ヤ": "ya", "ユ": "yu", "ヨ": "yo", "ラ": "ra", "リ": "ri", "ル": "ru", "レ": "re", "ロ": "ro", "ワ": "wa", "ヲ": "wo", "ン": "n", "ガ": "ga", "ギ": "gi", "グ": "gu", "ゲ": "ge", "ゴ": "go", "ザ": "za", "ジ": "ji", "ズ": "zu", "ゼ": "ze", "ゾ": "zo", "ダ": "da", "ヂ": "ji", "ヅ": "zu", "デ": "de", "ド": "do", "バ": "ba", "ビ": "bi", "ブ": "bu", "ベ": "be", "ボ": "bo", "パ": "pa", "ピ": "pi", "プ": "pu", "ペ": "pe", "ポ": "po", "キャ": "kya", "キュ": "kyu", "キョ": "kyo", "シャ": "sha", "シュ": "shu", "ショ": "sho", "チャ": "cha", "チュ": "chu", "チョ": "cho", "ニャ": "nya", "ニュ": "nyu", "ニョ": "nyo", "ヒャ": "hya", "ヒュ": "hyu", "ヒョ": "hyo", "ミャ": "mya", "ミュ": "myu", "ミョ": "myo", "リャ": "rya", "リュ": "ryu", "リョ": "ryo", "ギャ": "gya", "ギュ": "gyu", "ギョ": "gyo", "ジャ": "ja", "ジュ": "ju", "ジョ": "jo", "ビャ": "bya", "ビュ": "byu", "ビョ": "byo", "ピャ": "pya", "ピュ": "pyu", "ピョ": "pyo", "ヱ": "we", "ヰ": "wi"
        }
    else:
        raise ValueError(f"Chart is not valid: {chart_name}")

def update_buttons():
    global chart, buttons
    chart_name = chart_combo.get()
    chart = create_chart(chart_name)

    for button in buttons:
        button.destroy()
    buttons = []

    hiragana_items = list(chart.items())
    random.shuffle(hiragana_items)

    row = 0
    col = 0

    for hiragana, romaji in hiragana_items:
        button = create_button(window, hiragana, romaji, row, col)
        buttons.append(button)
        col += 1
        if col > 9:
            col = 0
            row += 1
    shuffle_buttons()

window = tk.Tk()
window.title("Learn and memorize Hiragana/Katakana")
window.geometry("1280x720")

style = ttk.Style()
style.theme_use('clam')

button_font = tkFont.Font(family="Arial")
style.configure("TButton", font=button_font, padding=10)

for i in range(16):
    window.grid_rowconfigure(i, weight=1)
for i in range(10):
    window.grid_columnconfigure(i, weight=1)

control_frame = ttk.Frame(window, padding=(10, 5))
control_frame.grid(row=15, column=0, columnspan=10, sticky="nsew")

chart_label = ttk.Label(control_frame, text="")
chart_label.grid(row=0, column=0, sticky="w", padx=(0,5))

chart_combo = ttk.Combobox(control_frame, values=["hiragana", "katakana"], state="readonly")
chart_combo.current(0)
chart_combo.grid(row=0, column=1, sticky="ew", padx=(0,50))
chart_combo.bind("<<ComboboxSelected>>", lambda event: update_buttons())

control_frame.grid_columnconfigure(2, weight=1)
control_frame.grid_columnconfigure(3, weight=1)

shuffle_button = ttk.Button(control_frame, text="Randomize", command=shuffle_buttons)
shuffle_button.grid(row=0, column=2, sticky="ew", padx=(0,5))

reveal_all_button = ttk.Button(control_frame, text="Show/Hide", command=reveal_all)
reveal_all_button.grid(row=0, column=3, sticky="ew")

chart = create_chart("hiragana")
buttons = []

update_buttons()

all_revealed = False

window.bind("<Configure>", update_font_size)
window.mainloop()
