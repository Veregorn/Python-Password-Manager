from tkinter import *
import math
from tkmacosx import Button

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#ffffff"
BACKGROUND = "#EDE9D0"
BLUE = "#03BEBF"
FONT_COLOR = "#620000"
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save(*entries):
    # Create a line var
    line = ""

    # Loop the arguments and add them to my var with the separator
    for i, field in enumerate(entries):
        if i < len(entries) - 1:
            line += field.get() + " | " # If not last add the separator
        else:
            line += field.get() # If last, not separator added
        # Finally, delete the content of the Entry
        field.delete(0, END)
        # If is the email, rewrite it
        if i == 0:
            field.insert(0, "rjbarco@gmail.com")

    # Finally add an "end of line"
    line += "\n"

    # Write the line to the file (append mode to add the line at the end of the file)
    with open('data.txt', 'a') as file:
        file.write(line)

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
website_entry = Entry(textvariable=website, width=35, highlightbackground=BACKGROUND, background=WHITE)
website_entry.grid(column=1, row=4, pady=10)

# Create an entry for the email/username
username = StringVar()
username_entry = Entry(textvariable=username, width=35, highlightbackground=BACKGROUND, background=WHITE)
username_entry.insert(0, "rjbarco@gmail.com")
username_entry.grid(column=1, row=1)

# Create an entry for the password
password = StringVar()
password_entry = Entry(textvariable=password, width=35, highlightbackground=BACKGROUND, background=WHITE)
password_entry.grid(column=1, row=2, pady=10)

# Create a button to generate a new password
password_button = Button(text="Generate Password", width=330, highlightbackground=BACKGROUND, background=BLUE, fg=WHITE, border=0, font=(FONT_NAME, 16, 'bold'))
password_button.grid(column=1, row=3, pady=10)

# Create a button to save data in file
# We are using lambda because otherwise we can't pass parameters to a command button function
add_button = Button(text="Add", width=330, highlightbackground=BACKGROUND, background=BLUE, fg=WHITE, border=0, font=(FONT_NAME, 16, 'bold'), command=lambda: save(username_entry, password_entry, website_entry))
add_button.grid(column=1, row=5, columnspan=2)










window.mainloop()