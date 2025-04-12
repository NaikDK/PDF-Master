from tkinter import *
from View.Main_Window import Main_Window 
class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Master")
        self.configure(background="lavender")
        self.option_add("*Label.foreground", "gray30")
        self.option_add("*Label.background", "lavender")
        self.option_add("*Button.foreground", "gray30")
        self.option_add("*Label.backforeground", "lavender")
        self.resizable(0, 0)
        Main_Window(self)
        self.create_widgets()

    def create_widgets(self):
        # Status bar
        self.status_var = StringVar()
        self.status = Label(
            self, textvariable=self.status_var, anchor="w"
        )
        self.status_var.set("Status: ")
        # self.status.grid(row=2, columnspan=3, padx=25, pady=5)
        self.status.pack(pady=20)

        # Author Line
        self.author_line = Label(
            self, text="Produced by: Deep Naik"
        )
        # self.author_line.grid(row=5, column=0, columnspan=4)
        self.author_line.pack(pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()