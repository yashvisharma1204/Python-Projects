from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("Datacom.csv")
    print(original_data)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Words", fill="white")
    canvas.itemconfig(card_word, text=current_card["def"], fill="white")
    canvas.itemconfig(card_background, image=card_front_img)

def flip_card():
    canvas.itemconfig(card_title, text="Definations", fill="black")
    canvas.itemconfig(card_word, text=current_card["words"], fill="black")
    canvas.itemconfig(card_background, image=card_back_img)

def flip_on_click():
    flip_card()

def is_known():
    to_learn.remove(current_card)
    print(len(to_learn))
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()

def known():
    next_card()

window = Tk()
window.title("Flash cards")
window.config(padx=50, pady=10, bg=BACKGROUND_COLOR)


canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="Untitled.png")
card_back_img = PhotoImage(file="2.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Times New Roman", 20, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Georgia", 18, "bold"),width=250)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=3)

cross_image = PhotoImage(file="no.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=flip_on_click)
unknown_button.grid(row=1, column=0)


check_image = PhotoImage(file="check.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=2)

next_button = Button(font="Monospace",text ="NEXT", command=known)
next_button.grid(row=1,column=1)



next_card()

window.mainloop()



