import random
import string
import tkinter as tk


def generate_password():
    # Define the character set to use for the password
    chars = string.ascii_letters + string.digits

    # Filter out unwanted characters
    chars = [c for c in chars if c not in 'lIo0O1']

    # Generate a random password by choosing characters from the character set
    first = ''.join(random.choice(chars) for i in range(5))
    second = ''.join(random.choice(chars) for i in range(5))
    third = ''.join(random.choice(chars) for i in range(5))
    fourth = ''.join(random.choice(chars) for i in range(5))

    # Join the sections together to form the complete password
    password = '-'.join([first, second, third, fourth])
    return password


def generate_passwords():
    # Clear the output text widget
    output_text.delete("1.0", tk.END)

    # Get the number of passwords to generate from the entry box
    amount = int(entry_amount.get())

    # Generate the specified number of passwords and add them to the output text widget
    for i in range(amount):
        password = generate_password()
        output_text.insert(tk.END, password + '\n')


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
output_text.grid(row=6, column=0, columnspan=3, sticky="we")

# Start the main loop of the GUI
root.mainloop()
