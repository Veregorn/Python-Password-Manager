from tkinter import *
from random import randint, choices, shuffle
from tkmacosx import Button
from tkinter import messagebox
import pyperclip
import json

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
def save():
    
    # Get the data we need
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    # Test if some field is empty, if yes, then inform and break the function
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Ooops", message="Please, fill all the fields")
        return
    else: # Create the new data dictionary
        new_data = {
            website: {
                "username": username,
                "password": password
            }
        }

    # Ask the user if he/she want to confirm the operation
    is_ok = messagebox.askokcancel(title="Information", message=f"These are the details entered: \nWebsite: {website}\nUsername: {username}\nPassword: {password}\nIs it ok to save?")

    if is_ok:
        try:
            # Open an read existing json file (open it in read mode)
            with open('data.json', 'r') as file:
                # Reading old data
                data = json.load(file)
        except FileNotFoundError: # If file doesn't exist, create it and write new data
            with open('data.json', 'w') as file:
                json.dump(new_data, file, indent=4) # So the info is indented in the file (easy readable)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4) # So the info is indented in the file (easy readable)
        finally:
            # Finally, delete the content of each Entry and set username to default email
            website_entry.delete(0, END)
            username_entry.delete(0, END)
            username_entry.insert(0, "rjbarco@gmail.com")
            password_entry.delete(0, END)

# ---------------------------- SEARCH FUNCTION ------------------------------- #
def find_password():
    # Get the data we need
    website = website_entry.get()

    # Try to open the file where data is saved
    try:
        with open('data.json', 'r') as file:
            # Read data
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            entry = data[website]
            messagebox.showinfo(title="Information", message=f"This is the data saved for the website {website}:\nUsername: {entry['username']}\nPassword: {entry['password']}")
        else:
            messagebox.showinfo(title="Information", message=f"No details for {website} exists.")

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
website_entry.grid(column=1, row=4, pady=10, columnspan=2)

# Create an entry for the email/username
username = StringVar()
username_entry = Entry(textvariable=username, width=35, highlightbackground=BACKGROUND, background=WHITE, fg=BLACK)
username_entry.insert(0, "rjbarco@gmail.com")
username_entry.grid(column=1, row=1, columnspan=2)

# Create an entry for the password
password = StringVar()
password_entry = Entry(textvariable=password, width=35, highlightbackground=BACKGROUND, background=WHITE, fg=BLACK)
password_entry.grid(column=1, row=2, pady=10, columnspan=2)

# Create a button to generate a new password
password_button = Button(text="Generate Password", width=320, highlightbackground=BACKGROUND, background=BLUE, fg=WHITE, border=0, font=(FONT_NAME, 16, 'bold'), command=generate_password)
password_button.grid(column=1, row=3, pady=10, columnspan=2)

# Create a button to save data in file
add_button = Button(text="Add", width=150, highlightbackground=BACKGROUND, background=BLUE, fg=WHITE, border=0, font=(FONT_NAME, 16, 'bold'), command=save)
add_button.grid(column=1, row=5, padx=10)

# Create a button to search if is there any info related what user has typed into 'Website' field
search_button = Button(text="Search", width=150, highlightbackground=BACKGROUND, background=BLUE, fg=WHITE, border=0, font=(FONT_NAME, 16, 'bold'), command=find_password)
search_button.grid(column=2, row=5, padx=10)









window.mainloop()