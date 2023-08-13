
import tkinter as tk

def change_color(entries, color):
    for entry in entries:
        entry.config(bg=color)

def checkbox_changed():
    if checkbox_var.get():
        change_color(entry_list, "light green")
    else:
        change_color(entry_list, "white")

# Create the main window
root = tk.Tk()
root.title("Entry Color Changer")

# Create Entry widgets
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry3 = tk.Entry(root)
entry4 = tk.Entry(root)
entry5 = tk.Entry(root)

entry_list = [entry1, entry2, entry3, entry4, entry5]

# Create a Checkbox
checkbox_var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Change Entry Colors", variable=checkbox_var, command=checkbox_changed)

# Pack the widgets
entry1.pack()
entry2.pack()
entry3.pack()
entry4.pack()
entry5.pack()
checkbox.pack()

# Run the main loop
root.mainloop()