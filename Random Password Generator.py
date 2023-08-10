import tkinter as tk
import random
import string
import pyperclip  # For copying to clipboard

def generate_password():
    password_length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    generated_password_label.config(text=generated_password)

    # Calculate password strength and set indicator text and color
    password_strength = calculate_password_strength(generated_password)
    strength_label.config(text=password_strength[0], fg=password_strength[1])

def calculate_password_strength(password):
    # Calculate password strength based on length and complexity
    length_factor = min(len(password) / 20, 1)  # Normalize length factor to be between 0 and 1
    complexity_factor = min(len(set(password)) / 20, 1)  # Normalize complexity factor to be between 0 and 1
    strength = length_factor * complexity_factor

    if strength >= 0.7:
        return ("Strong", "green")
    elif strength >= 0.4:
        return ("Moderate", "orange")
    else:
        return ("Weak", "red")

def copy_to_clipboard():
    password = generated_password_label.cget("text")
    pyperclip.copy(password)

# Create the main window
root = tk.Tk()
root.title("Random Password Generator")

# Length Entry
length_label = tk.Label(root, text="Length of password:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Generate Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Generated Password Box
generated_password_frame = tk.Frame(root, bd=2, relief="sunken")
generated_password_frame.pack(pady=10)
generated_password_label = tk.Label(generated_password_frame, text="", wraplength=300, font=("Arial", 12))
generated_password_label.pack(padx=10, pady=5)

# Password Strength Indicator
strength_label = tk.Label(root, text="", font=("Arial", 12))
strength_label.pack()

# Copy Button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

# Start the main event loop
root.mainloop()
