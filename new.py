import tkinter as tk

root = tk.Tk()
root.geometry("800x600")

frame = tk.Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

# Create widgets
label1 = tk.Label(frame, text="Label 1")
label2 = tk.Label(frame, text="Label 2")

# Configure grid weights
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

# Place widgets in grid
label1.grid(row=0, column=0, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)

root.mainloop()
