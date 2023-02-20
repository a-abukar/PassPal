import json
import hashlib
import re
import tkinter as tk
from tkinter import messagebox


# Define file name to save credentials
CREDENTIALS_FILE = 'credentials.json'


def save_credentials(username, password, hint, recovery_email):
    # load existing credentials
    try:
        with open(CREDENTIALS_FILE, 'r') as f:
            credentials = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        credentials = {}

    # hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # add new credential
    credentials[username] = {
        'password': hashed_password,
        'hint': hint,
        'recovery_email': recovery_email,
    }

    # save credentials to file
    with open(CREDENTIALS_FILE, 'w') as f:
        json.dump(credentials, f)


def authenticate_user(username, password):
    # load existing credentials
    try:
        with open(CREDENTIALS_FILE, 'r') as f:
            credentials = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return False

    # hash the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # check if the credentials match
    if username in credentials and credentials[username]['password'] == hashed_password:
        return True
    else:
        return False


class PasswordManager(tk.Tk):
    def __init__(self):
        super().__init__()

        # create GUI elements
        self.logo = tk.PhotoImage(file="logo.png")
        self.logo_label = tk.Label(self, image=self.logo)
        self.username_label = tk.Label(self, text="Username:")
        self.username_input = tk.Entry(self)
        self.password_label = tk.Label(self, text="Password:")
        self.password_input = tk.Entry(self, show="*")
        self.hint_label = tk.Label(self, text="Password Hint:")
        self.hint_input = tk.Entry(self)
        self.recovery_email_label = tk.Label(self, text="Recovery Email:")
        self.recovery_email_input = tk.Entry(self)
        self.sign_up_button = tk.Button(
            self, text="Sign Up", command=self.sign_up)
        self.log_in_button = tk.Button(
            self, text="Log In", command=self.log_in)

        # create layouts
        self.grid_columnconfigure(1, weight=1)
        self.logo_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.username_label.grid(row=1, column=0, padx=10, pady=10)
        self.username_input.grid(row=1, column=1, padx=10, pady=10)
        self.password_label.grid(row=2, column=0, padx=10, pady=10)
        self.password_input.grid(row=2, column=1, padx=10, pady=10)
        self.hint_label.grid(row=3, column=0, padx=10, pady=10)
        self.hint_input.grid(row=3, column=1, padx=10, pady=10)
        self.recovery_email_label.grid(row=4, column=0, padx=10, pady=10)
        self.recovery_email_input.grid(row=4, column=1, padx=10, pady=10)
        self.sign_up_button.grid(row=5, column=0, padx=10, pady=10)
        self.log_in_button.grid(row=5, column=1, padx=10, pady=10)

    def sign_up(self):
        # get user inputs
        username = self.username_input.get()
        password = self.password_input.get()
        hint = self.hint_input.get()
        recovery_email = self.recovery_email_input.get()

        # validate input
        if not username or not password or not hint or not recovery_email:
            messagebox.showwarning("Error", "Please fill in all fields.")
            return

        if len(password) < 8:
            messagebox.showwarning(
                "Error", "Password must be at least 8 characters long.")
            return

        # Check if password meets strong requirements
        uppercase_regex = r'[A-Z]'
        lowercase_regex = r'[a-z]'
        digit_regex = r'\d'
        special_char_regex = r'[-!$%^&*()_+|~=`{}\[\]:";\'<>?,.\/]'

        if (not re.search(uppercase_regex, password)
            or not re.search(lowercase_regex, password)
            or not re.search(digit_regex, password)
                or not re.search(special_char_regex, password)):
            messagebox.showwarning(
                "Error", "Password must contain at least one uppercase letter, one lowercase letter, one digit, and one special character (-!$%^&*()_+|~=`{}\[\]:\";'<>?,.\/).")
            return

        if len(password) > 128:
            messagebox.showwarning(
                "Error", "Password cannot be longer than 128 characters.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", recovery_email):
            messagebox.showwarning(
                "Error", "Please enter a valid email address.")
            return

        # save password
        save_credentials(username, password, hint, recovery_email)

        messagebox.showinfo("Success", "Password saved successfully.")

    def log_in(self):
        # get user inputs
        username = self.username_input.get()
        password = self.password_input.get()

        # authenticate user
        if authenticate_user(username, password):
            messagebox.showinfo("Success", f"Logged in as {username}.")
            # TODO: implement password management functionality
        else:
            messagebox.showwarning("Error", "Invalid username or password.")


if __name__ == '__main__':
    app = PasswordManager()
    app.title("PassPal")
    app.geometry("400x600")
    app.mainloop()
