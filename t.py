import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Horizontal Scrollable Frame")

# Create a canvas widget
canvas = tk.Canvas(root)
canvas.pack(fill=tk.BOTH, expand=True)

# Create a horizontal scrollbar
scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.xview)
scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

# Configure the canvas to scroll horizontally
canvas.configure(xscrollcommand=scrollbar.set)

# Create a frame inside the canvas
frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor=tk.NW)

# Add widgets to the scrollable frame
for i in range(50):
    label = ttk.Label(frame, text=f"Label {i}")
    label.grid(row=0, column=i, padx=10, pady=10)

# Bind the canvas to the frame resizing event
def resize_frame(event):
    canvas.configure(scrollregion=canvas.bbox("all"), width=event.width)

canvas.bind("<Configure>", resize_frame)

# Run the main application loop
root.mainloop()
