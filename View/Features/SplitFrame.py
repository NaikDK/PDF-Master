from tkinter import *

class SplitFrame(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background="lavender")
        self.controller = controller
        self.files = []
        self.create_merge_widgets()
    
    def create_merge_widgets(self):
        pass