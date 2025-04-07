import tkinter as tk
class Main_Window(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.pack()
        self.create_base()
    
    def create_base(self):
        pass