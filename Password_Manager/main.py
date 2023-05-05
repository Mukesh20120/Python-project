import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project


def Generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letter

    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_entry.insert(0, f"{password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #


def Saving_password():
    website_text = website_entry.get()
    email_text = Email_entry.get()
    password_text = password_entry.get()
    new_data = {
        website_text : {
             "email" : email_text,
             "password" : password_text
    }
    }
    if len(website_text) == 0 or len(password_text) == 0:
        messagebox.showinfo(title="Oops", message="Make sure you haven't left any field empty?")
    else:
        is_ok = messagebox.askokcancel(title="Confirmation",
                                           message=f"These details you entered- \n Website: {website_text} \n Email: {email_text} \n Password: {password_text} \n is it OK?")
        if is_ok:
            try:
                with open("data_password.json", mode="r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data_password.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("data_password.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

def find_password():
    website_find = website_entry.get()
    try:
        with open("data_password.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="File not found")
    else:
        if website_find in data:
            get_email = data[website_find]["email"]
            get_pass = data[website_find]["password"]
            messagebox.showinfo(title="Your Password", message=f"email : {get_email}\n password: {get_pass}")
        else:
            messagebox.showinfo(title="Not found", message=f"{website_find} website password not found.")
# ---------------------------- find password ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=250, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

#label
website = Label(text="Website:")
website.grid(column=0, row=1)
Email = Label(text="Email/Username:")
Email.grid(column=0, row=2)
password = Label(text="Password:")
password.grid(column=0, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1)
website_entry.focus()
Email_entry = Entry(width=35)
Email_entry.grid(column=1, row=2)
Email_entry.insert(0, "xyz@gmail.com")
Email_entry.index(END)
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)

#Button
search_btn = Button(text="Search", command=find_password)
search_btn.grid(column=2, row=1)
Generate_btn = Button(text="Generate", command=Generate_password)
Generate_btn.grid(column=2, row=3)
Add_btn = Button(text="ADD", width=40, command=Saving_password)
Add_btn.grid(column=1, row=4, columnspan=2)

window.mainloop()
