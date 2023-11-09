import tkinter
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


def main():
    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    # Password Generator Project
    def generate_password():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_list = []
        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

        password_list = password_numbers + password_letters + password_symbols
        shuffle(password_list)
        password = "".join(password_list)
        password_entry.delete(0,"end")
        password_entry.insert(0,password)
        pyperclip.copy(password)
    # ---------------------------- SAVE PASSWORD ------------------------------- #

    def delete_entry():
        website_entry.delete(0, 'end')
        password_entry.delete(0, 'end')

    def check_fields():
        website_check = website_entry.get()
        password_check = password_entry.get()
        if len(website_check) == 0 or len(password_check) == 0:
            messagebox.showwarning(title="Oops", message="Please don`t leave any fields empty")
            return False
        else:
            return True

    def save_password():
        fields_ok = check_fields()
        if fields_ok:
            website = website_entry.get()
            password = password_entry.get()
            login = login_entry.get()
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail:{login}"
                                                                  f"\nPassword:{password}"
                                                                  f"\nIs it ok to save?")
        if is_ok:
            file = open("password.txt", "a")
            file.write(f"\n{website} | {login} | {password} ")
            file.close()
            delete_entry()

    # ---------------------------- UI SETUP ------------------------------- #
    # Main Window
    window = tkinter.Tk()
    window.title("Password Manager")
    window.config(pady=20, padx=20)

    # Canvas Image
    canvas = tkinter.Canvas()
    canvas.config(height=200, width=200)
    locker_img = tkinter.PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=locker_img)
    canvas.grid(column=1, row=0)

    # Website Label
    website_label = tkinter.Label(text="Website:")
    website_label.grid(column=0, row=1)

    # Website Entry
    website_entry = tkinter.Entry(width=35)
    website_entry.focus()
    website_entry.grid(column=1, row=1, columnspan=2)

    # Email/Username Label
    login_label = tkinter.Label(text="Email/Username:")
    login_label.grid(column=0, row=2)

    # Email/Username Entry
    login_entry = tkinter.Entry(width=35)
    login_entry.insert(0, "default@gmail.com")
    login_entry.focus()
    login_entry.grid(column=1, row=2, columnspan=2)

    # Password Label
    password_label = tkinter.Label(text="Password:")
    password_label.grid(column=0, row=3)

    # Password Entry
    password_entry = tkinter.Entry(width=21)
    password_entry.focus()
    password_entry.grid(column=1, row=3)

    # Generate Password Button
    password_btn = tkinter.Button(text="Generate Password", padx=0, pady=0,command=generate_password)
    password_btn.grid(column=2, row=3)

    # Add Button
    add_btn = tkinter.Button(text="Add", width=36, command=save_password)
    add_btn.grid(column=1, row=4, columnspan=2)

    window.mainloop()


if __name__ == '__main__':
    main()
