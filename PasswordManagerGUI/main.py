from tkinter import *
from tkinter import messagebox
import random
from symbols import symbols
import json


# ------------------- OPERATIONS ------------------ #
def generate():
    password = []
    for i in range(random.randint(8, 10)):
        password.append(random.choice(random.choice(symbols)))
    password_entry.delete(0, END)
    password_entry.insert(0, "".join(password))

def export_data():
    export_flag = True
    website = website_entry.get()
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "username": username,
            "password": password,
        }
    }
    if website == "":
        website_entry.config(highlightcolor="Red", highlightbackground="Red")
        export_flag = False
    if email == "":
        email_entry.config(highlightcolor="Red", highlightbackground="Red")
        export_flag = False
    if username == "":
        username_entry.config(highlightcolor="Red", highlightbackground="Red")
        export_flag = False
    if password == "":
        password_entry.config(highlightcolor="Red", highlightbackground="Red")
        export_flag = False
    if export_flag:
        website_entry.config(highlightcolor="White")
        email_entry.config(highlightcolor="White")
        username_entry.config(highlightcolor="White")
        password_entry.config(highlightcolor="White")
    if export_flag:
        is_ok = messagebox.askokcancel(title=website,
                                       message="You have entered: \n"
                                               "Email: {}\n"
                                               "Username: {}\n"
                                               "Password: {}\n"
                                               "Export fields?".format(email, username, password))
        if is_ok:
            try:
                with open("data.json", "r") as data_file_read:
                    data = json.load(data_file_read)
            except FileNotFoundError:
                with open("data.json", "w") as data_file_write:
                    json.dump(new_data, data_file_write, indent=4)
            else:
                if website in data:
                    data.pop(website)
                    data[website] = new_data
                else:
                    data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)

def search_and_fill():
    website = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        website_dict = data[website]
    except FileNotFoundError:
        website_entry.delete(0, END)
        website_entry.insert(0, "No data")
    except KeyError:
        email_entry.config(highlightcolor="Red", highlightbackground="Red")
        username_entry.config(highlightcolor="Red", highlightbackground="Red")
        password_entry.config(highlightcolor="Red", highlightbackground="Red")
    else:
        email_entry.delete(0, END)
        email_entry.insert(0, website_dict["email"])
        username_entry.delete(0, END)
        username_entry.insert(0, website_dict["username"])
        password_entry.delete(0, END)
        password_entry.insert(0, website_dict["password"])


# -------------------- UI SETUP ------------------- #
# Window
window = Tk()
window.title("Random Password Generator")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=224, highlightthickness=False)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 112, image=logo)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ")
website_label.focus()
website_label.grid(column=0, row=1)
email_label = Label(text="Email: ")
email_label.grid(column=0, row=2)
username_label = Label(text="Username: ")
username_label.grid(column=0, row=3)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=4)

# Entries
website_entry = Entry(width=24)
website_entry.grid(column=1, row=1)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
username_entry = Entry(width=35)
username_entry.grid(column=1, row=3, columnspan=2)
password_entry = Entry(width=24)
password_entry.grid(column=1, row=4)

# Buttons
search_button = Button(text="Search", command=search_and_fill, width=7)
search_button.grid(column=2, row=1)
generate_button = Button(text="Generate", command=generate, width=7)
generate_button.grid(column=2, row=4)
export_button = Button(text="Export Fields", command=export_data)
export_button.grid(column=1, row=5)

# Keep UI up
window.mainloop()
