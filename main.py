import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    are_empty = len(website) == 0 or len(email) == 0 or len(password) == 0

    if are_empty:
        error = messagebox.showerror(title="Error", message="Please fill all the fields")
        if error == "ok":
            return
    else:
        pass

    is_ok = messagebox.askokcancel(title=website,
                                   message=f"This are the details entered\n{email} \n{password} \nIs it ok to save ")
    if is_ok:

        try:
            with open('data.json', 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


    website_input.focus()

    pyperclip.copy(password)


# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

START_EMAIL = "adam.choynowski1@gmail.com"

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

my_img = PhotoImage(file="logo.png")
# Canvas
canvas = Canvas()
canvas.config(width=200, height=200)
canvas.create_image(1, 1, image=my_img, anchor='nw')
canvas.grid(row=0, column=1)

# Labels
website_text = Label(text="Website:")
website_text.grid(row=1, column=0)
email_text = Label(text="Email/Username:")
email_text.grid(row=2, column=0)
password_text = Label(text="Password:")
password_text.grid(row=3, column=0)

# Entries
website_input = Entry(width=35)
website_input.focus()
website_input.grid(row=1, column=1, columnspan=2, sticky="EW")
email_input = Entry(width=35)
email_input.insert(0, START_EMAIL)
email_input.grid(row=2, column=1, columnspan=2, sticky="EW")
password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="EW")

# Buttons
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="EW")

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
