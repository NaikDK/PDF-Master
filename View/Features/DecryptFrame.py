from tkinter import *

class DecryptFrame(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background="lavender")
        self.create_widgets()

    def create_widgets(self):
        # Create widgets for the DecryptFrame
        self.label = Label(self, text="Decrypt PDF")
        self.label.pack(pady=20)

        # Add more widgets as needed