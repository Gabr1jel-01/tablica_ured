import tkinter as tk
import json

# List to store row data
rows_data = []

# Function to add a new row of entry widgets
def add_row():
    new_row = [tk.Entry(frame) for _ in range(4)]
    rows_data.append(new_row)
    
    for col, entry in enumerate(new_row):
        entry.grid(row=len(rows_data), column=col)

# Function to remove the last row of entry widgets
def remove_row():
    if rows_data:
        last_row = rows_data.pop()
        for entry in last_row:
            entry.destroy()

# Function to save the rows and their data
def save_rows_data():
    # Filter out any rows that have been deleted
    filtered_rows_data = [row for row in rows_data if all(entry.winfo_exists() for entry in row)]
    
    with open("rows_data.json", "w") as file:
        json.dump(filtered_rows_data, file, default=lambda x: x.get())

# Function to load the rows and their data
def load_rows_data():
    try:
        with open("rows_data.json", "r") as file:
            loaded_data = json.load(file)
            for row_data in loaded_data:
                add_row()
                for col, entry in enumerate(row_data):
                    rows_data[-1][col].insert(0, entry)
    except FileNotFoundError:
        pass

# Create the main application window
app = tk.Tk()
app.title("Row Data App")

# Create a frame to contain the entry widgets
frame = tk.Frame(app)
frame.pack()

# Create "Add Row" and "Remove Row" buttons
add_button = tk.Button(app, text="Add Row", command=add_row)
remove_button = tk.Button(app, text="Remove Row", command=remove_row)
save_button = tk.Button(app, text="Save Rows Data", command=save_rows_data)

# Load the rows and their data when the app starts
load_rows_data()

# Pack the buttons
add_button.pack()
remove_button.pack()
save_button.pack()

# Start the Tkinter main loop
app.mainloop()
