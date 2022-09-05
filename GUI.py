from cProfile import label
from tkinter import *


window = Tk()  
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 1, image=logo_img)
canvas.grid(row=0, column=1)

#Labels - grid-class
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Enteries - related to entry-class not the grid-class
website_entry = Entry(width=37)
website_entry.grid(row=1, column=1, columnspan=2)
email_entry = Entry(width=37)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Buttons
generate_password_button = Button(text="Generate Password")
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36)
add_button.grid(row=4, column=1, columnspan=2)







window.mainloop()