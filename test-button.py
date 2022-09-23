
from cProfile import label
from tkinter import *
from main import *
# import easygui

# ----------------- Window, Canvas and image --------------- #

window = Tk()  
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(height=300, width=300)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=logo_img)
canvas.pack()
canvas.grid(row=0, column=0)

# --------------- Buttons ------------------ #

pm = PasswordManager()
# myvar = easygui.enterbox("What, is your favorite color?")



# Not currently in use - but try to use this to take user input for path (as required by the create_key functions)
def path():
    frame = Tk()
    frame.title("Please Enter File Path")
    frame.geometry('400x200')

    inputtxt = Text(frame, height = 5, width = 20)

    def test():
        entry_text = StringVar()
        path.entry = Entry(frame, width=10, textvariable=entry_text)

    inputtxt.pack()

    enterButton = Button(frame, text = "Enter file path", command=test)
    enterButton.pack()

    lbl = Label(frame, text = "")
    lbl.pack()

    frame.mainloop()

# class tinkerButton:

#     def __init__(self):
#         self.inp = None
    
#     def path(self, inp):
#         frame = Tk()
#         frame.title("Please Enter File Path")
#         frame.geometry('400x200')

#         inputtxt = Text(frame, height = 5, width = 20)

#         inp = inputtxt.get(1.0, "end-1c")
#         # lbl.config(text = "Your chosen path is: "+inp)

#         # def test():
#         #     entry_text = tk.StringVar()
#         #     path.entry = tk.Entry(frame, width=10, textvariable=entry_text)

#         inputtxt.pack()

#         enterButton = Button(frame, text = "Enter file path", command=inp)
#         enterButton.pack()

#         lbl = Label(frame, text = "")
#         lbl.pack()

#         frame.mainloop()


# create_key_button = Button(text="Create a new key", command=lambda : pm.create_key(input("Enter file path: ")))
create_key_button = Button(text="Create a new key", command=lambda : pm.create_key(input("Enter file path: ")))
create_key_button.grid(row=1, column=0)

load_key_button = Button(text="Load existing key")
load_key_button.grid(row=2, column=0)

create_pass_button = Button(text="Create a new password file")
create_pass_button.grid(row=3, column=0)

load_pass_button = Button(text="Load existing password file")
load_pass_button.grid(row=4, column=0)

add_pass_button = Button(text="Add a new password")
add_pass_button.grid(row=5, column=0)

get_pass_button = Button(text="Get a password")
get_pass_button.grid(row=6, column=0)

quit_button = Button(text="Quit")
quit_button.grid(row=7, column=0)


window.mainloop()


