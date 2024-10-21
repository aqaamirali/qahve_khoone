from tkinter import *
from random import *
import json
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# window
window = Tk()
window.title("Password Manager")
window.config(padx=100, pady=100)
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)
saved_password = ""


# password

def pass_generator():
    letters = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f', 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K',
               'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u',
               'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '&', '(', ')', '+', '^', '*']
    random_letters = [choice(letters) for item in range(randint(8, 10))]
    random_numbers = [choice(numbers) for item in range(randint(2, 4))]
    random_symbols = [choice(symbols) for item in range(randint(2, 4))]
    password = random_letters + random_numbers + random_symbols
    shuffle(password)
    password_str = "".join(password)
    password_entry.insert(0, string=password_str)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pressed():
    global saved_password
    email = email_username_entry.get()
    password = password_entry.get()
    website = website_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }
    saved_password = f"{website} | {email} | {password}\n"
    if len(website) == 0:
        messagebox.showerror(title="oops", message="you left website field empty!")
    elif len(password) == 0:
        messagebox.showerror(title="oops", message="you left password field empty!")
    else:
        print(saved_password)
        try:
            with open("passwords.json", "r") as data_file:
                data = json.load(data_file)
                if website in data:
                    answer=messagebox.askquestion(title="duplicate website", message="this website has already saved.\n"
                    "do yuo want to replace the password?")
                    if answer == "yes":
                        data.update(new_data)
                else:
                    data.update(new_data)
            with open("passwords.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        except FileNotFoundError:
            with open("passwords.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        finally:
            website_entry.delete(first=0, last=END)
            password_entry.delete(first=0, last=END)


# ---------------------------- SEARCH ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="you have not saved any data")
    else:
        if website in data:
            saved_email = data[website]["email"]
            saved_pass = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {saved_email}\nPassword: {saved_pass}")
        else:
            messagebox.showerror(title="Error", message=" you have not saved any data by this website")



# ---------------------------- UI SETUP ------------------------------- #


website_txt = Label(text="Website:")
website_txt.grid(column=0, row=1)

website_entry = Entry(width=16)
website_entry.focus()
website_entry.grid(column=1, row=1)

email_username_txt = Label(text="Email/Username:")
email_username_txt.grid(column=0, row=2)

email_username_entry = Entry(width=35)
email_username_entry.insert(END, string="isazadeh2004@gmail.com")
email_username_entry.grid(column=1, row=2, columnspan=2)

password_txt = Label(text="Password:")
password_txt.grid(column=0, row=3)

password_entry = Entry(width=16)
password_entry.grid(column=1, row=3)

pass_generator_button = Button(text="Generator Password", command=pass_generator)
pass_generator_button.grid(column=2, row=3)

add_button = Button(text="Add", width=30, command=add_pressed)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password)
search_button.grid(row=1, column=2)

window.mainloop()
