import tkinter as tk
from tkinter import Menu, scrolledtext, filedialog

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text.delete(1.0, tk.END)
            text.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text.get(1.0, tk.END))

# Create the main window
root = tk.Tk()
root.title("Text Editor")

menu_bar = Menu(root)
root.config(menu=menu_bar)

# Create File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=lambda: text.event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: text.event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: text.event_generate("<<Paste>>"))

view_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="View", menu=view_menu)
view_menu.add_command(label="Zoom In")
view_menu.add_command(label="Zoom Out")

text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
text.pack(expand=True, fill="both")


root.mainloop()
