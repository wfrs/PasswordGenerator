import random
import string
import tkinter as tk


def get_password_chars():
    # Define the character set to use for the password
    chars = string.ascii_letters + string.digits

    # Filter out unwanted characters
    chars = [c for c in chars if c not in 'lIo0O1']

    return chars


def generate_password():
    # Get the character set to use for the password
    chars = get_password_chars()

    # Generate a random password by choosing characters from the character set
    sections = [''.join(random.choice(chars)
                        for i in range(5)) for j in range(4)]
    password = '-'.join(sections)

    return password


def generate_passwords():
    # Clear the output text widget
    output_text.delete("1.0", tk.END)

    # Get the number of passwords to generate from the entry box
    amount = int(entry_amount.get())
    if amount > 1000:
        amount = 1000
    # Generate the specified number of passwords and add them to the output text widget
    passwords = [generate_password() for i in range(amount)]
    output_text.insert(tk.END, '\n'.join(passwords))
    passwords = []


# Create the main window and add a title
root = tk.Tk()
root.title("Password Generator")

# Create a label for the number of passwords to generate
label_amount = tk.Label(root, text="Number of passwords to generate:")
label_amount.grid(row=0, column=0)

# Create an entry box for the number of passwords
entry_amount = tk.Entry(root)
entry_amount.grid(row=0, column=1)

# Create a button to generate passwords
button_generate = tk.Button(
    root, text="Generate passwords", command=generate_passwords)
button_generate.grid(row=1, column=0, columnspan=2)

# Create a text widget to display the generated passwords
output_text = tk.Text(root, highlightbackground="gray", highlightthickness=1)
output_text.grid(row=2, column=0, columnspan=2, sticky="we")

# Start the main loop of the GUI
root.mainloop()
