from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
cur_card = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global cur_card, flip_timer
    window.after_cancel(flip_timer)
    cur_card = random.choice(to_learn)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word_txt, text=cur_card["French"], fill="black")
    canvas.itemconfig(background_img, image=bg_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word_txt, text=cur_card["English"], fill="white")
    canvas.itemconfig(background_img, image=back_img)


def is_known():
    to_learn.remove(cur_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
bg_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
background_img = canvas.create_image(400, 263, image=bg_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_txt = canvas.create_text(400, 263, text="", font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

cross_img = PhotoImage(file="images/wrong.png")
unknown_btn = Button(image=cross_img, command=next_card)
unknown_btn.grid(row=1, column=0)

check_img = PhotoImage(file="images/right.png")
known_btn = Button(image=check_img, command=is_known)
known_btn.grid(row=1, column=1)

next_card()
window.mainloop()
