<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 20:16:12 2023

@author: shreya
"""
#Password generator is a useful tool that generates strong and random passwords for users.password generator application using Python, allow users to specify the length and complexity of their password.
#import necessary libraries and modules

import tkinter as tk 
from tkinter import ttk, messagebox  #tkinter for GUI, ttk for themed widgets and message box too
import random
import string

#Define the generate_password function, which is called when the "Generate Password" button is clicked. It retrieves the selected options from the GUI, generates a password based on those options, and updates the displayed password.
def generate_password():
    length = int(length_var.get())
    set_up_uppercase = uppercase_var.get()
    set_up_lowercase = lowercase_var.get()
    set_up_digits = digits_var.get()
    set_up_special = special_var.get()

    characters = ""
    if set_up_uppercase:
        characters += string.ascii_uppercase
    if set_up_lowercase:
        characters += string.ascii_lowercase
    if set_up_digits:
        characters += string.digits
    if set_up_special:
        characters += string.punctuation

    if not characters:
        messagebox.showinfo("Sorry", "Please select at least one category","It is mandatory")
        return

    your_password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(your_password)

def copy_to_clipboard():   #It copies the generated password to the clipboard and shows a message indicating success.
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Done.", "Password copied to clipboard!")

# GUI setup
#Create the main Tkinter window (root) and set its title. Create a frame (frame) to organize widgets, add padding, and place it in the window.
root = tk.Tk()  #create the main window.Root is the common name for main window
root.title("Password Generator") #title appears in the title bar of the window

frame = ttk.Frame(root, padding="15") #frames and other widgets in main window. ttk module is used for themed Tkinter components. The frame is given a padding of 15 pixels.
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S)) #grid layout. The grid method is used to place the frame at column 0, row 0 of the grid. The sticky parameter determines how the frame should expand to fill the available space; in this case, it will expand in all directions (West, East, North, South).

# Password Length
ttk.Label(frame, text="Length of your Password:").grid(column=0, row=0, sticky=tk.W) #creates a themed Tkinter label widget within the frame
length_var = tk.StringVar(value="10")
length_entry = ttk.Entry(frame, textvariable=length_var)
length_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))
#The grid method is then used to specify its position in the grid layout: column 0, row 0. The sticky parameter ensures that the label sticks to the West side of its grid cell.
# It is initialized with the default value of "10", representing the default length for the password.But allows you to erase and enter any desired number.
#The last line specifies the grid layout for the entry widget. It is placed in column 1, row 0. The sticky parameter is set to (tk.W, tk.E), indicating that the entry widget should expand horizontally to the West and East within its grid cell.


# Character Types
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)
# initializes variables with the value True.You can deselect the checkbox

ttk.Checkbutton(frame, text="Uppercase", variable=uppercase_var).grid(column=0, row=1, sticky=tk.W)
ttk.Checkbutton(frame, text="Lowercase", variable=lowercase_var).grid(column=1, row=1, sticky=tk.W)
ttk.Checkbutton(frame, text="Digits", variable=digits_var).grid(column=0, row=2, sticky=tk.W)
ttk.Checkbutton(frame, text="Special Characters", variable=special_var).grid(column=1, row=2, sticky=tk.W)

# Generate Button
generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(column=0, row=3, columnspan=2, pady=(10, 0))
#This code creates a themed Tkinter button labeled "Generate Password" within the previously defined frame. The button is associated with the generate_password function, which is presumably defined elsewhere in the code. The button is positioned in the grid at column 0, row 3, and spans two columns (columnspan=2). The pady parameter adds vertical padding, pushing the button down by 10 pixels. When clicked, this button will trigger the execution of the generate_password function, presumably responsible for generating a password based on the user's specified criteria.

# Generated Password
password_var = tk.StringVar(value="")
ttk.Entry(frame, textvariable=password_var, state="readonly").grid(column=0, row=4, columnspan=2, pady=(10, 0))
#This code sets up a Tkinter StringVar (password_var) initialized with an empty string. It then creates a themed Tkinter entry widget within the previously defined frame. This entry widget is associated with the password_var variable, allowing it to display and be updated based on the contents of the variable. The entry widget is set to "readonly" state, indicating that the user cannot directly edit its content. It is positioned in the grid at column 0, row 4, spanning two columns (columnspan=2). Additionally, vertical padding of 10 pixels (pady=(10, 0)) is applied, pushing the entry widget down. This entry widget is likely intended to display the generated password, and its content will be updated by the program when the user generates a new password using the specified criteria.

# Copy to Clipboard Button
copy_button = ttk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(column=0, row=5, columnspan=2, pady=(10, 0))

# Run the GUI
root.mainloop()
=======
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 20:16:12 2023

@author: shreya
"""
#Password generator is a useful tool that generates strong and random passwords for users.password generator application using Python, allow users to specify the length and complexity of their password.
#import necessary libraries and modules

import tkinter as tk 
from tkinter import ttk, messagebox  #tkinter for GUI, ttk for themed widgets and message box too
import random
import string

#Define the generate_password function, which is called when the "Generate Password" button is clicked. It retrieves the selected options from the GUI, generates a password based on those options, and updates the displayed password.
def generate_password():
    length = int(length_var.get())
    set_up_uppercase = uppercase_var.get()
    set_up_lowercase = lowercase_var.get()
    set_up_digits = digits_var.get()
    set_up_special = special_var.get()

    characters = ""
    if set_up_uppercase:
        characters += string.ascii_uppercase
    if set_up_lowercase:
        characters += string.ascii_lowercase
    if set_up_digits:
        characters += string.digits
    if set_up_special:
        characters += string.punctuation

    if not characters:
        messagebox.showinfo("Sorry", "Please select at least one category","It is mandatory")
        return

    your_password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(your_password)

def copy_to_clipboard():   #It copies the generated password to the clipboard and shows a message indicating success.
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    root.update()
    messagebox.showinfo("Done.", "Password copied to clipboard!")

# GUI setup
#Create the main Tkinter window (root) and set its title. Create a frame (frame) to organize widgets, add padding, and place it in the window.
root = tk.Tk()  #create the main window.Root is the common name for main window
root.title("Password Generator") #title appears in the title bar of the window

frame = ttk.Frame(root, padding="15") #frames and other widgets in main window. ttk module is used for themed Tkinter components. The frame is given a padding of 15 pixels.
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S)) #grid layout. The grid method is used to place the frame at column 0, row 0 of the grid. The sticky parameter determines how the frame should expand to fill the available space; in this case, it will expand in all directions (West, East, North, South).

# Password Length
ttk.Label(frame, text="Length of your Password:").grid(column=0, row=0, sticky=tk.W) #creates a themed Tkinter label widget within the frame
length_var = tk.StringVar(value="10")
length_entry = ttk.Entry(frame, textvariable=length_var)
length_entry.grid(column=1, row=0, sticky=(tk.W, tk.E))
#The grid method is then used to specify its position in the grid layout: column 0, row 0. The sticky parameter ensures that the label sticks to the West side of its grid cell.
# It is initialized with the default value of "10", representing the default length for the password.But allows you to erase and enter any desired number.
#The last line specifies the grid layout for the entry widget. It is placed in column 1, row 0. The sticky parameter is set to (tk.W, tk.E), indicating that the entry widget should expand horizontally to the West and East within its grid cell.


# Character Types
uppercase_var = tk.BooleanVar(value=True)
lowercase_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
special_var = tk.BooleanVar(value=True)
# initializes variables with the value True.You can deselect the checkbox

ttk.Checkbutton(frame, text="Uppercase", variable=uppercase_var).grid(column=0, row=1, sticky=tk.W)
ttk.Checkbutton(frame, text="Lowercase", variable=lowercase_var).grid(column=1, row=1, sticky=tk.W)
ttk.Checkbutton(frame, text="Digits", variable=digits_var).grid(column=0, row=2, sticky=tk.W)
ttk.Checkbutton(frame, text="Special Characters", variable=special_var).grid(column=1, row=2, sticky=tk.W)

# Generate Button
generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
generate_button.grid(column=0, row=3, columnspan=2, pady=(10, 0))
#This code creates a themed Tkinter button labeled "Generate Password" within the previously defined frame. The button is associated with the generate_password function, which is presumably defined elsewhere in the code. The button is positioned in the grid at column 0, row 3, and spans two columns (columnspan=2). The pady parameter adds vertical padding, pushing the button down by 10 pixels. When clicked, this button will trigger the execution of the generate_password function, presumably responsible for generating a password based on the user's specified criteria.

# Generated Password
password_var = tk.StringVar(value="")
ttk.Entry(frame, textvariable=password_var, state="readonly").grid(column=0, row=4, columnspan=2, pady=(10, 0))
#This code sets up a Tkinter StringVar (password_var) initialized with an empty string. It then creates a themed Tkinter entry widget within the previously defined frame. This entry widget is associated with the password_var variable, allowing it to display and be updated based on the contents of the variable. The entry widget is set to "readonly" state, indicating that the user cannot directly edit its content. It is positioned in the grid at column 0, row 4, spanning two columns (columnspan=2). Additionally, vertical padding of 10 pixels (pady=(10, 0)) is applied, pushing the entry widget down. This entry widget is likely intended to display the generated password, and its content will be updated by the program when the user generates a new password using the specified criteria.

# Copy to Clipboard Button
copy_button = ttk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(column=0, row=5, columnspan=2, pady=(10, 0))

# Run the GUI
root.mainloop()
>>>>>>> 112fc8c4dd908cf213b413f494ebe4d96c81586d
