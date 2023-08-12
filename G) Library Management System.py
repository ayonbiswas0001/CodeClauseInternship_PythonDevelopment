import tkinter as tk

class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.issued_copies = 0
        self.issued_student = None

class LibraryManagementSystem:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def delete_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return f"Book '{book.title}' deleted successfully."
        return "Book not found in the library."

    def view_available_books(self):
        available_books = [book for book in self.books if book.copies > book.issued_copies]
        return available_books

    def issue_book(self, book_title, student_name):
        for book in self.books:
            if book.title == book_title and book.copies > book.issued_copies:
                book.issued_copies += 1
                return f"Book '{book.title}' issued to {student_name}."
        return "Book not available for issuing."

    def return_book(self, book_title, student_name):
        for book in self.books:
            if book.title == book_title and book.issued_copies > 0:
                book.issued_copies -= 1
                return f"Book '{book.title}' returned by {student_name}."
        return "Book not found or not issued to the student."


# Function to search for a book
def search_book():
    keyword = search_entry.get().lower()
    search_results.delete(1.0, tk.END)  # Clear previous results

    for book in library.books:
        if keyword in book.title.lower() or keyword in book.author.lower() or keyword in book.isbn.lower():
            result = f"Book Title: {book.title}\n"
            result += f"Author: {book.author}\n"
            result += f"ISBN: {book.isbn}\n"
            result += f"Available Copies: {book.copies - book.issued_copies}\n\n"
            search_results.insert(tk.END, result)

# Create a library management system instance
library = LibraryManagementSystem()

# Function to add books
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    isbn = isbn_entry.get()
    copies = int(copies_entry.get())
    if title and author and isbn and copies > 0:
        book = Book(title, author, isbn, copies)
        library.add_book(book)
        status_label.config(text="Book added successfully.")
        refresh_list()
    else:
        status_label.config(text="Please fill in all fields and provide valid number of copies.")


# Function to delete a book
def delete_book():
    title = delete_title_entry.get()
    amount = int(delete_amount_entry.get())
    for book in library.books:
        if book.title == title:
            if amount <= book.copies - book.issued_copies:
                book.copies -= amount
                status = library.delete_book(book)
                status_label.config(text=status)
                refresh_list()
                return
            else:
                status_label.config(text="Cannot delete more copies than available.")
                return
    status_label.config(text="Book not found in the library.")


# Function to issue a book
def issue_book():
    title = issue_title_entry.get()
    student_name = student_name_entry.get()
    for book in library.books:
        if book.title == title and book.copies > book.issued_copies:
            book.issued_copies += 1
            book.issued_student = student_name
            status = f"Book '{book.title}' issued to {student_name}."
            status_label.config(text=status)
            refresh_list()
            return
    status_label.config(text="Book not available for issuing.")

# Function to return a book
def return_book():
    title = return_title_entry.get()
    student_name = return_student_name_entry.get()
    for book in library.books:
        if book.title == title and book.issued_copies > 0:
            if book.issued_student == student_name:
                book.issued_copies -= 1
                book.issued_student = None
                status = f"Book '{book.title}' returned by {student_name}."
                status_label.config(text=status)
                refresh_list()
                return
            else:
                status_label.config(text="Book can only be returned by the student who issued it.")
                return
    status_label.config(text="Book not found or not issued to the student.")


# Function to refresh the list of available books
def refresh_list():
    available_books = library.view_available_books()
    result_text.delete(1.0, tk.END)
    if available_books:
        for book in available_books:
            result_text.insert(tk.END, f"Title: {book.title}\nAuthor: {book.author}\nISBN: {book.isbn}\nAvailable Copies: {book.copies - book.issued_copies}\n\n")
    else:
        result_text.insert(tk.END, "No available books in the library.")
        

# Create the main window
root = tk.Tk()
root.title("Library Management System")


# Create labels and entry widgets for adding books
num_books_label = tk.Label(root, text="Number of books to add:")
num_books_label.grid(row=0, column=0)
copies_entry = tk.Entry(root)
copies_entry.grid(row=0, column=1)

title_label = tk.Label(root, text="Title:")
title_label.grid(row=1, column=0)
title_entry = tk.Entry(root)
title_entry.grid(row=1, column=1)

author_label = tk.Label(root, text="Author:")
author_label.grid(row=2, column=0)
author_entry = tk.Entry(root)
author_entry.grid(row=2, column=1)

isbn_label = tk.Label(root, text="ISBN:")
isbn_label.grid(row=3, column=0)
isbn_entry = tk.Entry(root)
isbn_entry.grid(row=3, column=1)

add_button = tk.Button(root, text="Add Book", command=add_book)
add_button.grid(row=4, column=0, columnspan=2)

# Create labels and entry widgets for deleting a book
delete_title_label = tk.Label(root, text="Enter the title of the book to delete:")
delete_title_label.grid(row=5, column=0)
delete_title_entry = tk.Entry(root)
delete_title_entry.grid(row=5, column=1)

delete_amount_label = tk.Label(root, text="Enter the number of copies to delete:")
delete_amount_label.grid(row=6, column=0)
delete_amount_entry = tk.Entry(root)
delete_amount_entry.grid(row=6, column=1)

delete_button = tk.Button(root, text="Delete Book", command=delete_book)
delete_button.grid(row=8, column=0, columnspan=2)


# Create labels and entry widgets for issuing a book
issue_title_label = tk.Label(root, text="Enter the title of the book to issue:")
issue_title_label.grid(row=9, column=0)
issue_title_entry = tk.Entry(root)
issue_title_entry.grid(row=9, column=1)

student_name_label = tk.Label(root, text="Enter student's name:")
student_name_label.grid(row=10, column=0)
student_name_entry = tk.Entry(root)
student_name_entry.grid(row=10, column=1)

issue_button = tk.Button(root, text="Issue Book", command=issue_book)
issue_button.grid(row=11, column=0, columnspan=2)


# Create labels and entry widgets for returning a book
return_title_label = tk.Label(root, text="Enter the title of the book to return:")
return_title_label.grid(row=12, column=0)
return_title_entry = tk.Entry(root)
return_title_entry.grid(row=12, column=1)

return_student_name_label = tk.Label(root, text="Enter student's name:")
return_student_name_label.grid(row=13, column=0)
return_student_name_entry = tk.Entry(root)
return_student_name_entry.grid(row=13, column=1)

return_button = tk.Button(root, text="Return Book", command=return_book)
return_button.grid(row=14, column=0, columnspan=2, padx=10, pady=10)


# Create a Text widget to display search results
search_results = tk.Text(root, wrap=tk.WORD, width=60, height=9)
search_results.grid(row=17, column=0, columnspan=2, padx=10, pady=10)


# Create a text widget to display available books
result_text = tk.Text(root, width=60, height=10)
result_text.grid(row=16, column=0, columnspan=2, padx=10, pady=10)


# Create a button to refresh the list of available books
refresh_button = tk.Button(root, text="Refresh List", command=refresh_list)
refresh_button.grid(row=26, column=0, columnspan=2)

# Refresh the list of available books on startup
refresh_list()


# Function to search for books and display results
def search_book():
    keyword = search_entry.get().lower()
    search_results.delete(1.0, tk.END)  # Clear previous results

    for book in library.books:
        if keyword in book.title.lower() or keyword in book.author.lower() or keyword in book.isbn.lower():
            result = f"Book Title: {book.title}\n"
            result += f"Author: {book.author}\n"
            result += f"ISBN: {book.isbn}\n"
            result += f"Available Copies: {book.copies - book.issued_copies}\n\n"
            search_results.insert(tk.END, result)
        else:
            search_results.insert(tk.END, "No matching books found.")


# Create a button to search for books
search_button = tk.Button(root, text="Search", command=search_book)
search_button.grid(row=15, column=0, columnspan=2, padx=10, pady=10)



# Create UI components for book search
search_label = tk.Label(root, text="Search Book:")
search_entry = tk.Entry(root)
search_button = tk.Button(root, text="Search", command=search_book)
status_label = tk.Label(root, text="", fg="blue")

# Layout UI components for book search
search_label.place(x=70, y=325)  # Adjust coordinates as needed
search_entry.place(x=335, y=325)  # Adjust coordinates as needed
#search_button.place(x=475, y=323)  # Adjust coordinates as needed
status_label.place(x=500, y=500)  # Adjust coordinates as needed

# Create a status label to show messages
status_label = tk.Label(root, text="", fg="red")
status_label.grid(row=228, column=100, columnspan=20)

# Create a Text widget to display search results
#search_results = tk.Text(root, wrap=tk.WORD)
#search_results.place(x=150, y=550, width=200, height=80)


# Start the main event loop
root.mainloop()
