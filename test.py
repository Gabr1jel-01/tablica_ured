import tkinter as tk

class CustomFrame:
    def __init__(self, parent, width, height):
        self.width = width
        self.height = height
        self.frame = tk.Frame(parent, width=self.width, height=self.height, bg="lightblue")
        self.frame.pack()

class CustomWindow:
    def __init__(self, width, height, title="Custom Window"):
        self.width = width
        self.height = height
        self.title = title

        self.window = tk.Tk()
        self.window.title(self.title)
        self.window.geometry(f"{self.width}x{self.height}")

        self.add_frame_button = tk.Button(self.window, text="Add Frame", command=self.add_custom_frame)
        self.add_frame_button.pack(pady=20)

    def add_custom_frame(self):
        custom_frame = CustomFrame(self.window, 200, 150)  # You can customize the frame's size
        custom_frame.frame.pack()

    def run(self):
        self.window.mainloop()

# Example usage:
if __name__ == "__main__":
    my_window = CustomWindow(400, 300, "My Custom Window")
    my_window.run()
