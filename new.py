import tkinter as tk
from tkinter import messagebox

class CustomApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dictionary App")

        self.my_dict = {}  # Initialize an empty dictionary

        self.label = tk.Label(root, text="Enter Key:")
        self.label.pack()

        self.key_entry = tk.Entry(root)
        self.key_entry.pack()

        self.label = tk.Label(root, text="Enter Value:")
        self.label.pack()

        self.value_entry = tk.Entry(root)
        self.value_entry.pack()

        self.add_button = tk.Button(root, text="Add Key-Value", command=self.add_key_value)
        self.add_button.pack()

    def add_key_value(self):
        key = self.key_entry.get()
        value = self.value_entry.get()

        if key and value:
            self.my_dict[key] = value
            messagebox.showinfo("Success", f"Added: '{key}': '{value}' to the dictionary.")
        else:
            messagebox.showwarning("Error", "Both key and value must be entered.")

if __name__ == "__main__":
    root = tk.Tk()
    app = CustomApp(root)
    root.mainloop()
