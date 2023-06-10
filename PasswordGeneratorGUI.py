import customtkinter
from tkinter import messagebox
import random

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# Functions
def no_special_characters_password(password_length):
    password = []
    while password_length >= 0:
        capital_letter = chr(random.randint(ord('A'), ord('Z')))
        lower_letter = chr(random.randint(ord('a'), ord('z')))
        number = random.randint(0,9)
        vars = [capital_letter, lower_letter, number]
        password_element = random.choice(vars)
        password.append(str(password_element))
        password_length -= 1
    password[:] = [''.join(password[:])]
    return messagebox.showinfo('Generated!', 'Your password is: ' + str(*password))

def special_characters_password(password_length):
    password = []
    special_characters = ['!','"','#','$','%','&']
    while password_length >= 0:
        capital_letter = chr(random.randint(ord('A'), ord('Z')))
        lower_letter = chr(random.randint(ord('a'), ord('z')))
        number = random.randint(0,9)
        character = random.choice(special_characters)
        vars = [capital_letter, lower_letter, number, character]
        password_element = random.choice(vars)
        password.append(str(password_element))
        password_length -= 1
    password[:] = [''.join(password[:])]
    return messagebox.showinfo('Generated', 'Your password is: ' + str(*password))

def generate():
    try:
        int(response.get())
        if int(response.get()) > 0:
            if check_state.get() == 0:
                return no_special_characters_password(int(response.get()))
            else:
                return special_characters_password(int(response.get()))
        else:
            return messagebox.showinfo('NegRedo', 'Please input a positive integer.')
    except:
        return messagebox.showinfo('Redo', 'Please input a digit(s).')

# Application
app = customtkinter.CTk()
app.geometry("600x200")
app.title("Vince's Password Generator")

# Interface
question = customtkinter.CTkLabel(app, font=('Roboto', 20, "bold"), text="How many characters would you like your password to be?")
question.pack(padx=10, pady=10)

response = customtkinter.StringVar()
textbox = customtkinter.CTkEntry(app, textvariable=response)
textbox.pack(padx=10, pady=10)

check_state = customtkinter.IntVar()

checkbox = customtkinter.CTkCheckBox(app, text="Special Characters?", variable=check_state)
checkbox.pack(padx=10, pady=10)

button = customtkinter.CTkButton(app, font=('Roboto', 12, "italic"), text="GENERATE", command=generate)
button.pack(padx=10, pady=10)

# Launching
app.mainloop()