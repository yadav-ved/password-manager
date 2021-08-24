import random
from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def genrate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
               'V', 'W', 'X', 'Y', 'Z']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']


    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_nymbers = [choice(numbers) for _ in range(randint(2,4))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]

    password_list = password_letters + password_nymbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = websit_input.get()
    email = user_input.get()
    password = pass_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message= " please make sure you haven't left any files empty.")

    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered : \n Email: {email}\n Passoed: {password} \n Is it ok to save?  ")
        if is_ok:
            with open("Data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                websit_input.delete(0, END)
                pass_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 100, pady = 80)

canvas = Canvas(height = 200, width = 200)
log_img = PhotoImage(file = "logo.png")
canvas.create_image(100, 100,image = log_img)
canvas.grid(column = 1, row = 1)

websit_label = Label(text = "websit: ")
websit_label.grid(column = 0, row = 2)
websit_input = Entry(width = 55)
websit_input.grid(column = 1, row = 2, columnspan = 2)
websit_input.focus()

user_lable = Label(text = "Email/UserName: ")
user_lable.grid(column = 0, row = 3)
user_input = Entry(width = 55)
user_input.grid(column = 1, row = 3, columnspan =2)
user_input.insert(0,"@gmail.com")

pass_label = Label(text = "Password: ")
pass_label.grid(column = 0, row = 4)
pass_input = Entry(width = 35)
pass_input.grid(column = 1, row = 4)

create_button = Button(text = "Genrate Passworsd", command = genrate_password)
create_button.grid(column = 2, row = 4)

add_button = Button(width = 45, text = "ADD", command = save)
add_button.grid(column = 1, row = 5, columnspan =2)


window.mainloop()