from tkinter import *


def helper():
    miles_value = float(entry.get())
    km_value = miles_value * 1.609
    kilometer["text"] = f"{km_value}"


window = Tk()
window.minsize()
window.config(padx=20, pady=20)
window.title("Convert Miles to Kilometer")

entry = Entry(width=7)
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal = Label(text="to equal to ")
equal.grid(column=0, row=1)

kilometer = Label(text="0")
kilometer.grid(column=1, row=1)

km = Label(text="Km")
km.grid(column=2, row=1)

btn = Button(text="Calculate", command=helper)
btn.grid(column=2, row=2)

window.mainloop()
