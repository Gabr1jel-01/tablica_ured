import tkinter as tk

def on_checkbox_click(checkbox_id):
    if checkbox_var[checkbox_id].get() == 1:
        print(f"Checkbox {checkbox_id} is marked")
    else:
        print(f"Checkbox {checkbox_id} is not marked")

def add_checkbox():
    global checkbox_count
    checkbox_id = checkbox_count
    checkbox_var[checkbox_id] = tk.IntVar()
    checkbox = tk.Checkbutton(root, text=f"Checkbox {checkbox_id}", variable=checkbox_var[checkbox_id], command=lambda id=checkbox_id: on_checkbox_click(id))
    checkbox.pack()
    checkbox_count += 1

root = tk.Tk()
root.title("Checkbox Example")

checkbox_var = {}
checkbox_count = 0

add_button = tk.Button(root, text="Add Checkbox", command=add_checkbox)
add_button.pack()

root.mainloop()
