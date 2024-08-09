from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

DEFAULT_EMAIL = "dummy.@examplemail.com"
DATA_FILE = "data.json"
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
SYMBOLS = '!#$%&()*+'

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_characters = (
        [choice(LETTERS) for _ in range(randint(8, 10))] +
        [choice(SYMBOLS) for _ in range(randint(2, 4))] +
        [choice(NUMBERS) for _ in range(randint(2, 4))]
    )
    shuffle(password_characters)
    password = "".join(password_characters)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data(data):
    with open(DATA_FILE, "w") as data_file:
        json.dump(data, data_file, indent=4)

def load_data():
    try:
        with open(DATA_FILE, "r") as data_file:
            return json.load(data_file)
    except FileNotFoundError:
        return {}

def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    description = description_entry.get().strip()

    if not website or not password:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
        return

    new_data = {website: {"email": email, "password": password, "description": description}}
    data = load_data()
    data.update(new_data)
    save_data(data)

    website_entry.delete(0, END)
    password_entry.delete(0, END)
    description_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get().strip()
    data = load_data()

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        description = data[website]["description"]
        messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}\nDescription: {description}")
    else:
        messagebox.showinfo(title="Error", message=f"No details for {website} exist.")

# ---------------------------- UI SETUP ------------------------------- #

def setup_ui():
    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    canvas = Canvas(window, height=200, width=200)
    logo_img = PhotoImage(file="icons8-lock-200.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1)

    # Labels
    Label(window, text="Website:").grid(row=1, column=0)
    Label(window, text="Email/Username:").grid(row=2, column=0)
    Label(window, text="Password:").grid(row=3, column=0)
    Label(window, text="Description:").grid(row=4, column=0)

    # Entries
    global website_entry, email_entry, password_entry, description_entry
    website_entry = Entry(window, width=21)
    website_entry.grid(row=1, column=1)
    website_entry.focus()

    email_entry = Entry(window, width=35)
    email_entry.grid(row=2, column=1, columnspan=2)
    email_entry.insert(0, DEFAULT_EMAIL)

    password_entry = Entry(window, width=21)
    password_entry.grid(row=3, column=1)

    description_entry = Entry(window, width=35)
    description_entry.grid(row=4, column=1, columnspan=2)

    # Buttons
    Button(window, text="Search", width=13, command=find_password).grid(row=1, column=2)
    Button(window, text="Generate Password", command=generate_password).grid(row=3, column=2)
    Button(window, text="Add", width=36, command=save).grid(row=5, column=1, columnspan=2)

    window.mainloop()

if __name__ == "__main__":
    setup_ui()
