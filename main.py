from tkinter import *
from random import randint, choices, shuffle
from tkmacosx import Button
from tkinter import messagebox
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#ffffff"
BLACK = "#000000"
BACKGROUND = "#EDE9D0"
BLUE = "#03BEBF"
FONT_COLOR = "#620000"
FONT_NAME = "Courier"
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Function that generates a random password with 8-10 letters, 2-4 symbols and 2-4 numbers
def generate_password():
    global password_entry

    # Password will have an aleatory number of characters
    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    # Selecting random picks from every list
    password_list = []
    password_list = choices(LETTERS, k=nr_letters)
    password_list += choices(SYMBOLS, k=nr_symbols)
    password_list += choices(NUMBERS, k=nr_numbers)

    # Shuffles the list
    shuffle(password_list)

    # From list to string
    password = "".join(password_list)

    # Edit the field
    password_entry.insert(0, password)

    # Copy the password to the clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
# This save function is flexible because you could pass it a variable number of fields
def save(*entries):
    # Create a line var
    line = ""

    # Loop the arguments and add them to my var with the separator
    for i, field in enumerate(entries):
        # Test if some field is empty, if yes, then inform and break the function
        if len(field.get()) == 0:
            messagebox.showerror(title="Ooops", message="Please, fill all the fields")
            return
        if i < len(entries) - 1:
            line += field.get() + " | " # If not last add the separator
        else:
            line += field.get() # If last, not separator added

    # Finally add an "end of line"
    line += "\n"

    # Ask the user if he/she want to confirm the operation
    is_ok = messagebox.askokcancel(title="Information", message=f"These are the details entered: \n {line}\nIs it ok to save?")

    if is_ok:
        # Write the line to the file (append mode to add the line at the end of the file)
        with open('data.txt', 'a') as file:
            file.write(line)
        # Finally, delete the content of each Entry
        for i, field in enumerate(entries):
            field.delete(0, END)
            # Rewrite email field with the default value
            if i == 0:
                field.insert(0, "rjbarco@gmail.com")


# ---------------------------- UI SETUP ------------------------------- #
# Create the App window
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg=BACKGROUND)

# Create a canvas to put an image on it
canvas = Canvas(window, width=200, height=220, bg=BACKGROUND, highlightthickness=0)

# Create a locker image
locker_img = PhotoImage(file="logo.png")

# Put the image into the canvas
canvas.create_image(100, 100, image=locker_img)

# Finally, we need to position the canvas into the screen
canvas.grid(column=0, row=0, columnspan=2)

# Create a label for the website name
website_label = Label(text="Website:",font=(FONT_NAME, 18, 'bold'), bg=BACKGROUND, fg=FONT_COLOR)
website_label.grid(column=0, row=4)

# Create a label for the email/username
username_label = Label(text="Email/Username:",font=(FONT_NAME, 18, 'bold'), bg=BACKGROUND, fg=FONT_COLOR)
username_label.grid(column=0, row=1)

# Create a label for the password
password_label = Label(text="Password:",font=(FONT_NAME, 18, 'bold'), bg=BACKGROUND, fg=FONT_COLOR)
password_label.grid(column=0, row=2)

# Create an entry for the website
website = StringVar()
website_entry = Entry(textvariable=website, width=35, highlightbackground=BACKGROUND, background=WHITE, fg=BLACK)
website_entry.grid(column=1, row=4, pady=10)

# Create an entry for the email/username
username = StringVar()
username_entry = Entry(textvariable=username, width=35, highlightbackground=BACKGROUND, background=WHITE, fg=BLACK)
username_entry.insert(0, "rjbarco@gmail.com")
username_entry.grid(column=1, row=1)

# Create an entry for the password
password = StringVar()
password_entry = Entry(textvariable=password, width=35, highlightbackground=BACKGROUND, background=WHITE, fg=BLACK)
password_entry.grid(column=1, row=2, pady=10)

# Create a button to generate a new password
password_button = Button(text="Generate Password", width=330, highlightbackground=BACKGROUND, background=BLUE, fg=WHITE, border=0, font=(FONT_NAME, 16, 'bold'), command=generate_password)
password_button.grid(column=1, row=3, pady=10)

# Create a button to save data in file
# We are using lambda because otherwise we can't pass parameters to a command button function
add_button = Button(text="Add", width=330, highlightbackground=BACKGROUND, background=BLUE, fg=WHITE, border=0, font=(FONT_NAME, 16, 'bold'), command=lambda: save(username_entry, password_entry, website_entry))
add_button.grid(column=1, row=5, columnspan=2)










window.mainloop()