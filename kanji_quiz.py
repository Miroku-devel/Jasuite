import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import random

def create_chart(chart_name):
    if chart_name == "JLPT N5":
        return {
            "日": "sun", "一": "one", "国": "country", "人": "person", "年": "year",
            "大": "big", "十": "ten", "二": "two", "本": "book", "中": "middle",
            "長": "long", "出": "exit", "三": "three", "時": "time", "行": "go",
            "見": "see", "月": "moon", "分": "minute", "後": "after", "前": "before",
            "生": "life", "五": "five", "間": "space", "上": "above", "東": "east",
            "四": "four", "今": "now", "金": "gold", "九": "nine", "入": "enter",
            "学": "study", "高": "high", "円": "yen", "子": "child", "外": "outside",
            "八": "eight", "六": "six", "下": "below", "来": "come", "気": "spirit",
            "小": "small", "七": "seven", "山": "mountain", "話": "talk", "女": "woman",
            "北": "north", "午": "noon", "百": "hundred", "書": "write", "先": "previous",
            "名": "name", "川": "river", "千": "thousand", "水": "water", "半": "half",
            "男": "man", "西": "west", "電": "electricity", "校": "school", "語": "word",
            "土": "earth", "木": "tree", "聞": "hear", "食": "eat", "車": "car", "何": "what",
            "南": "south", "万": "ten thousand", "毎": "every", "白": "white", "天": "heaven",
            "母": "mother", "火": "fire", "右": "right", "読": "read", "友": "friend",
            "左": "left", "休": "rest", "父": "father", "雨": "rain"
        }
    elif chart_name == "JLPT N4":
        return {
            "会": "meeting", "同": "same", "事": "matter", "自": "oneself", "社": "company",
            "発": "departure", "者": "someone", "地": "ground", "業": "business", "方": "direction",
            "新": "new", "場": "location", "員": "employee", "立": "stand up", "開": "open",
            "手": "hand", "力": "power", "問": "question", "代": "substitute", "明": "bright",
            "動": "move", "京": "capital", "目": "eye", "通": "traffic", "言": "say",
            "理": "logic", "体": "body", "田": "rice field", "主": "lord", "題": "topic",
            "意": "idea", "不": "negative", "作": "make", "用": "utilize", "度": "degrees",
            "強": "strong", "公": "public", "持": "hold", "野": "plains", "以": "by means of",
            "思": "think", "家": "house", "世": "generation", "多": "many", "正": "correct",
            "安": "safe", "院": "institution", "心": "heart", "界": "world", "教": "teach",
            "文": "sentence", "元": "beginning", "重": "heavy", "近": "near", "考": "consider",
            "画": "brush-stroke", "海": "sea", "売": "sell", "知": "know", "道": "road-way",
            "集": "gather", "別": "separate", "物": "thing", "使": "use", "品": "goods",
            "計": "plot", "死": "death", "特": "special", "私": "private", "始": "commence",
            "朝": "morning", "運": "carry", "終": "end", "台": "pedestal", "広": "wide",
            "住": "dwell", "無": "nothingness", "真": "true", "有": "possess", "口": "mouth",
            "少": "few", "町": "town", "料": "fee", "工": "craft", "建": "build",
            "空": "empty", "急": "hurry", "止": "stop", "送": "escort", "切": "cut",
            "転": "revolve", "研": "polish", "足": "leg", "究": "research", "楽": "music",
            "起": "wake up", "着": "arrive", "店": "store", "病": "ill", "質": "substance"
}
    else:
        raise ValueError(f"Chart name not valid: {chart_name}")

def gen_answer(chart):
    global correct_kanji, correct_meaning
    kanji_keys = list(chart.keys())
    if not kanji_keys:
        label.config(text="Empty chart!", foreground="black")
        for i in range(4):
            buttons[i].config(text="", command=None)
        return
    correct_kanji = random.choice(kanji_keys)
    correct_meaning = chart[correct_kanji]
    label.config(text=correct_kanji, foreground="black")

    meanings_opts = [correct_meaning]
    while len(meanings_opts) < 4:
        wrong_kanji = random.choice(kanji_keys)
        wrong_meaning = chart[wrong_kanji]
        if wrong_meaning not in meanings_opts:
            meanings_opts.append(wrong_meaning)

    random.shuffle(meanings_opts)

    for i in range(4):
        buttons[i].config(text=meanings_opts[i], command=lambda choice=meanings_opts[i]: check_answer(choice, chart))

def check_answer(choice, chart):
    if choice == correct_meaning:
        gen_answer(chart)
    else:
        label.config(foreground="red")

def update_font_size(event=None):
    font_size_button = int(min(window.winfo_width(), window.winfo_height()) / 25)
    button_font.config(size=max(font_size_button, 8))
    style.configure("TButton", font=button_font, padding=font_size_button // 4)

    font_size_label = int(min(window.winfo_width(), window.winfo_height()) / 4)
    label_font.config(size=max(font_size_label, 24))

def chart_changed(*args):
    try:
        selected_chart_name = chart_var.get()
        current_chart = create_chart(selected_chart_name)
        gen_answer(current_chart)
    except ValueError as e:
        print(e)
        label.config(text=str(e), foreground="red")
        for i in range(4):
            buttons[i].config(text="", command=None)


window = tk.Tk()
window.title("Learn and memorize Kanji")
window.geometry("400x400")

style = ttk.Style()
style.theme_use('clam')

label_font = tkFont.Font(family="Arial")
button_font = tkFont.Font(family="Arial")

label = ttk.Label(window, font=label_font, anchor="center")
label.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)

frame_buttons_lines = []
for r in range(2):
    frame_line = ttk.Frame(window)
    frame_line.grid(row=1 + r, column=0, sticky="nsew", padx=5)
    frame_buttons_lines.append(frame_line)
    window.grid_rowconfigure(1 + r, weight=1)

buttons = []
for r in range(2):
    for c in range(2):
        button = ttk.Button(frame_buttons_lines[r])
        button.grid(row=0, column=c, padx=5, pady=5, sticky="nsew")
        frame_buttons_lines[r].grid_columnconfigure(c, weight=1)
        buttons.append(button)

window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=3)
for row in range(1, 3):
    window.grid_rowconfigure(row, weight=1)

chart_var = tk.StringVar(window)
chart_options = ["JLPT N5", "JLPT N4"]
chart_var.set(chart_options[0])
chart_dropdown = ttk.Combobox(window, textvariable=chart_var, values=chart_options, state="readonly")
chart_dropdown.grid(row=4, column=0, pady=(10,30))
chart_var.trace("w", chart_changed)

current_chart = create_chart(chart_var.get())
gen_answer(current_chart)

window.bind("<Configure>", update_font_size)
window.mainloop()
