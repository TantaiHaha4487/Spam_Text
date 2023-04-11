import tkinter as tk
from customtkinter import CTkEntry, CTkButton


class MyApplication:
    def __init__(self, master):
        self.master = master

        # Create a CTkEntry widget
        self.entry = CTkEntry(self.master, width=20)
        self.entry.pack()

        # Create a CTkButton widget
        self.button = CTkButton(self.master, text="Submit", command=self.submit)
        self.button.pack()

        # Bind the Enter key to the entry widget
        self.entry.bind("<Return>", self.submit)

    def submit(self, event=None):
        # Handle the submit event
        text = self.entry.get()
        print("Submitted:", text)


root = tk.Tk()
app = MyApplication(root)
root.mainloop()