#Import library 
from cryptography.fernet import Fernet

class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}

    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f: # open path in writing bytes mode, and set as f
            f.write(self.key) # saving the key to a file
#       print(self.key)

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()

    def create_password_file(self, path, initial_values=None):
        self.password_file = path
        
        if initial_values is not None:
            for key, value in initial_values.items(): # List of tuples to be iterated
                self.add_password(key, value)

    def load_password_file(self, path):
        self.password_file = path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted = line.split(":")
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted.encode()).decode()

    def add_password(self, site, password):
        self.password_dict[site] = password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted = Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode() + "\n")

    def get_password(self, site):
        return self.password_dict[site]


def main():
    # Pre-populate passwords
    password = {
        "email": "hello",
        "discord": "discordpass",
        "apple": "applepass"
    }

    pm = PasswordManager()

    print("""What do you want to do?
    (1) Create a new key
    (2) Load an existing key
    (3) Create a new password file
    (4) Load existing password file
    (5) Add a new password
    (6) Get a password
    (q) Quit
    """)

    done = False

    while not done:

        choice = input("Enter your choice: ")
        if choice == "1":
            path = input("Enter path: ")
            pm.create_key(path)
        elif choice == "2":
            path = input("Enter path: ")
            pm.load_key(path)
        elif choice == "3":
            path = input("Enter path: ")
            pm.create_password_file(path, password)
        elif choice == "4":
            path = input("Enter path: ")
            pm.load_password_file(path)
        elif choice == "5":
            site = input("Enter the site: ")
            password = input("Enter the password: ")
            pm.add_password(site, password)
        elif choice == "6":
            site = input("What site do you want: ")
            print(f"Password for {site} js {pm.get_password(site)}")
        elif choice == "q":
            done = True
            print("Bye")
        else:
            print("Invalid choice")

# Run above script
if __name__ == "__main__":
    main()


#------------------------GUI-Section--------------------------#

# from tkinter import *


# window = Tk()  
# window.title("Password Manager")
# window.config(padx=20, pady=20)

# canvas = Canvas(height=200, width=200)
# logo_img = PhotoImage(file="logo.png")
# canvas.create_image(100, 1, image=logo_img)
# canvas.grid(row=0, column=1)

# #Labels - grid-class
# website_label = Label(text="Website:")
# website_label.grid(row=1, column=0)
# email_label = Label(text="Email/Username:")
# email_label.grid(row=2, column=0)
# password_label = Label(text="Password:")
# password_label.grid(row=3, column=0)

# #Enteries - related to entry-class not the grid-class
# website_entry = Entry(width=37)
# website_entry.grid(row=1, column=1, columnspan=2)
# email_entry = Entry(width=37)
# email_entry.grid(row=2, column=1, columnspan=2)
# password_entry = Entry(width=21)
# password_entry.grid(row=3, column=1)

# #Buttons
# generate_password_button = Button(text="Generate Password")
# generate_password_button.grid(row=3, column=2)
# add_button = Button(text="Add", width=36)
# add_button.grid(row=4, column=1, columnspan=2)






# window.mainloop()