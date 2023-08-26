import tkinter as tk

def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(event):
    current = entry.get()
    text = event.widget.cget("text")
    if text == "=":
        evaluate_expression() 
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry widget to display the expression and result
entry = tk.Entry(root, font=("Arial", 20))
entry.pack(padx=10, pady=10, ipadx=20, ipady=10)

# Create buttons for digits and operators
button_texts = [
    ("7", "8", "9", "/"),
    ("4", "5", "6", "*"),
    ("1", "2", "3", "-"),
    ("0", ".", "C", "+"),
    ("=",)
]

for row in button_texts:
    frame = tk.Frame(root)
    frame.pack()
    for text in row:
        button = tk.Button(frame, text=text, font=("Arial", 18), padx=20, pady=10)
        button.pack(side=tk.LEFT)
        button.bind("<Button-1>", button_click)

# Start the main event loop
root.mainloop()
