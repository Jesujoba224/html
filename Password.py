import tkinter as tk
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            password_label.config(text="Length must be positive")
            return

        chars = ""
        if uppercase_var.get():
            chars += string.ascii_uppercase
        if lowercase_var.get():
            chars += string.ascii_lowercase
        if digits_var.get():
            chars += string.digits
        if punctuation_var.get():
            chars += string.punctuation

        if not chars:
            password_label.config(text="Select at least one character type")
            return

        password = ''.join(random.choice(chars) for _ in range(length))
        password_label.config(text=password)
    except ValueError:
        password_label.config(text="Invalid length")

root = tk.Tk()
root.title("Random Password Generator")

length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

uppercase_var = tk.BooleanVar(value=True)
uppercase_check = tk.Checkbutton(root, text="Include Uppercase Letters", variable=uppercase_var)
uppercase_check.pack()

lowercase_var = tk.BooleanVar(value=True)
lowercase_check = tk.Checkbutton(root, text="Include Lowercase Letters", variable=lowercase_var)
lowercase_check.pack()

digits_var = tk.BooleanVar(value=True)
digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack()

punctuation_var = tk.BooleanVar(value=True)
punctuation_check = tk.Checkbutton(root, text="Include Special Characters", variable=punctuation_var)
punctuation_check.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

password_label = tk.Label(root, text="", font=("Arial", 12))
password_label.pack()

root.mainloop()