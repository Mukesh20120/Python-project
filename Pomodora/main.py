from tkinter import *
from math import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = NONE

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    window.after_cancel(timer)
    title_text.config(text="Timer")
    global rep
    rep = 0
    check_text.config(text="")
    canvas.itemconfig(counter_time, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    short_sec = SHORT_BREAK_MIN * 60
    long_sec = LONG_BREAK_MIN * 60

    if rep % 2 == 1:
        title_text.config(text="WORK", fg=RED)
        count_down(work_sec)
    elif rep % 8 == 0:
        title_text.config(text="Long Break", fg=PINK)
        count_down(long_sec)
    else:
        title_text.config(text="Short Break", fg=GREEN)
        count_down(short_sec)


def count_down(count):
    minute_left = floor(count/60)
    second_left = count % 60
    if second_left < 10:
        second_left = f'0{second_left}'
    canvas.itemconfig(counter_time, text=f"{minute_left}:{second_left}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark_rep = floor(rep/2)
        mark = ""
        for _ in range(mark_rep):
            mark += "✓"
        check_text.config(text=mark, fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodora")
window.config(padx=20, pady=20, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
counter_time = canvas.create_text(100, 113, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# canvas.pack()
canvas.grid(column=1, row=1)

title_text = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"))
title_text.grid(column=1, row=0)

start_btn = Button(text="Start", command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="Reset", command=reset_timer)
reset_btn.grid(column=2, row=2)


#check marks
check_text = Label(fg=GREEN, font=("Cursive", 20, "bold"))
check_text.grid(column=1, row=3)


window.mainloop()
