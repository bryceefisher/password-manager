from tkinter import *
from tkinter import messagebox
from random import choice
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def pass_generate():
    pass_entry.delete(0, "end")
    gen_pass = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789%^*(-_=+)!@#$&,.') for i in range(15)])
    pass_entry.insert(0, gen_pass)
    pyperclip.copy(gen_pass)
    messagebox.showinfo(title="Password Manager", message="Password copied to clipboard")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    # Assign entries to var
    web = website.get()
    em = email.get()
    word = password.get()

    # Check length var is greater than zero

    if len(web) == 0 or len(em) == 0 or len(word) == 0:
        messagebox.showinfo(title="Password Manager", message="Add a value for each entry to proceed.")
        return

    # User entry verification

    is_ok = messagebox.askokcancel(title=web,
                                   message=f"\nWebsite: {web}\nUsername: {em}\nPassword: {word}\n\n Would you like "
                                           f"to save?")
    if is_ok:
        with open("pass-data.csv", "a") as file:
            file.write(f"{web}, {em}, {word}\n")
        website_entry.delete(0, "end")
        pass_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Website Label
website_label = Label(text="Website:", font=("Arial", 12, "bold"))
website_label.grid(column=0, row=1)

# Website Entry
website = StringVar()
website_entry = Entry(textvariable=website)
website_entry.config(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.insert(0, "")
website_entry.focus()

# Email/Username Label
email_label = Label(text="Email/Username:", font=("Arial", 12, "bold"))
email_label.grid(column=0, row=2)

# Email Entry
email = StringVar()
email_entry = Entry(textvariable=email)
email_entry.config(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "")
email_entry.insert(0, "bryce.e.fisher@gmail.com")

# Password Label
password_label = Label(text="Password:", font=("Arial", 12, "bold"))
password_label.grid(column=0, row=3)

# Password Entry
password = StringVar()
pass_entry = Entry(textvariable=password)
pass_entry.config(width=22)
pass_entry.grid(column=1, row=3)
pass_entry.insert(0, "")

# Generate Button
gen_button = Button(text="Generate Password", font=("Arial", 10, "bold"), width=13, command=pass_generate)
gen_button.grid(column=2, row=3)

# Add Button
add_button = Button(text="Add", width=33, command=add_pass)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
