import tkinter as tk
from tkinter import filedialog
import json

def save_state():
    state = {
        "rows": [],
    }

    for row in rows:
        row_data = [entry.get() for entry in row]
        state["rows"].append(row_data)

    with open("app_state.json", "w") as file:
        json.dump(state, file)

def load_state():
    try:
        with open("app_state.json", "r") as file:
            state = json.load(file)

        for i, row_data in enumerate(state["rows"]):
            for j, cell_data in enumerate(row_data):
                rows[i][j].delete(0, tk.END)
                rows[i][j].insert(0, cell_data)

    except FileNotFoundError:
        # Handle the case where the file doesn't exist (e.g., first run)
        pass

def add_row():
    row = []
    for j in range(3):  # Change the number of columns as needed
        entry = tk.Entry(root)
        entry.grid(row=len(rows), column=j)
        row.append(entry)
    rows.append(row)

def delete_row():
    if rows:
        for entry in rows[-1]:
            entry.grid_forget()
        rows.pop()

# Create the main application window
root = tk.Tk()
root.title("Dynamic Table Application")

# Create a 2D list to store entry widgets
rows = []

# Load the previous state if it exists
load_state()

# Create buttons for adding and deleting rows
add_row_button = tk.Button(root, text="Add Row", command=add_row)
add_row_button.grid(row=0, column=0)

delete_row_button = tk.Button(root, text="Delete Row", command=delete_row)
delete_row_button.grid(row=0, column=1)

# Create Save button to save the current state
save_button = tk.Button(root, text="Save State", command=save_state)
save_button.grid(row=0, column=2)

# Start the Tkinter main loop
root.mainloop()
