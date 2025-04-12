from tkinter import *
from View.Features.MergeFrame import MergeFrame
from View.Features.DeletePagesFrame import DeletePagesFrame
from View.Features.DecryptFrame import DecryptFrame
from Controller.MergeController import MergeController
from Controller.DeleteController import DeleteController
from Controller.DecryptController import DecryptController

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
            "Decrypt Files"
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
            "Decrypt Files": DecryptFrame(self.frame_container, DecryptController())
        }
        
        self.current_frame = None
        self.selected_frame(self.drop.get())
        
    def selected_frame(self, frame_name):
        # frame_name = self.drop.get()
        if self.current_frame:
            self.current_frame.pack_forget()
        self.current_frame = self.frames[frame_name]
        self.current_frame.pack(fill="both", expand=True)