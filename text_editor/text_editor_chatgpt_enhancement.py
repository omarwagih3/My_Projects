import tkinter as tk
from tkinter import filedialog as fd

# Function to open a file and display its content in the text box
def open_file(text_box, window):
    file_path = fd.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_box.delete(1.0, tk.END)  # Clear the text box
            text_box.insert(tk.END, content)  # Insert the content into the text box
            window.title(f"Text Editor - {file_path}")  # Update the window title with the file path

# Function to save the content of the text box to a file
def save_as_file(text_box):
    file_path = fd.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            content = text_box.get(1.0, tk.END)
            file.write(content)

# Create the main window
root = tk.Tk()
root.title("Text Editor")  # Set the title of the window

# Create a text box that fills the entire window
text_box = tk.Text(root)
text_box.pack(fill="both", expand=True)

# Create a menu bar
menu_bar = tk.Menu(root)

# Create a "File" menu with "Open", "Save As", and "Exit" options
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=lambda: open_file(text_box, root))
file_menu.add_command(label="Save As", command=lambda: save_as_file(text_box))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Configure the menu bar
root.config(menu=menu_bar)

# Create a status bar at the bottom of the window
status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill="x")

# Add keyboard shortcuts for opening and saving files
root.bind('<Control-o>', lambda event: open_file(text_box, root))
root.bind('<Control-s>', lambda event: save_as_file(text_box))

# Run the application
root.mainloop()
