from tkinter import *
from View.Features.MergeFrame import MergeFrame
from View.Features.DeletePagesFrame import DeletePagesFrame
from Controller.MergeController import MergeController
from Controller.DeleteController import DeleteController

class Main_Window(Frame):
    def __init__(self, root):
        super().__init__(root)
        self.configure(background="lavender")
        self.pack(fill="both", expand=True, pady=20)
        self.create_base()
    
    def create_base(self):
        
        options = [
            "Merge Files",
            "Delete Pages",
            "Split PDF",
        ]
        self.drop = StringVar()
        self.drop.set(options[0])
        self.features = OptionMenu(self, self.drop, *options, command=self.selected_frame)
        self.features.pack()
        self.frame_container = Frame(self)
        self.frame_container.pack(fill="both", expand=True)

        self.frames = {
            "Merge Files": MergeFrame(self.frame_container, MergeController()),
            "Delete Pages": DeletePagesFrame(self.frame_container, DeleteController()),
            # "Split PDF",
        }
        
        self.current_frame = None
        self.selected_frame(self.drop.get())
        
    def selected_frame(self, frame_name):
        # frame_name = self.drop.get()
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.frames[frame_name]
        self.current_frame.pack(fill="both", expand=True)