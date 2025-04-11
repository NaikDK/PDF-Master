from tkinter import *

class DeletePagesFrame(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background="lavender")
        # self.pack(fill="both", expand=True)
        self.files = []
        self.create_delete_widgets()
    
    def create_delete_widgets(self):
        In_label = Label(
            self, text="Select input PDF: ", width="30", anchor="w", background="lavender"
        )
        In_selector = Button(self, text="Select PDF", command=self.add_pdf)
        pages_delete = StringVar()
        delete_label = Label(
            self,
            width="30",
            text="Pages to be deleted(, separated)",
            anchor="w",
            background="lavender",
        )
        pages_to_be_deleted = Entry(
            self, width="20", textvariable=pages_delete, background="misty rose"
        )
        deleted_file = Button(
            self, text="Delete Pages", command=self.delete_pages, state=DISABLED
        )
        download = Button(
            self, text=("Download file"), command=self.download_new_pdf, state=DISABLED
        )

        # Deletor widget placement Starts Here
        In_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        In_selector.grid(row=0, column=1, padx=5, pady=5)
        delete_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        pages_to_be_deleted.grid(row=1, column=1, padx=5, pady=5)
        deleted_file.grid(row=2, column=0, padx=5, pady=5)
        download.grid(row=2, column=1)

    def add_pdf(self, file):
        self.files.append(file)

    def delete_pages(self):
        pass

    def download_new_pdf(self):
        pass

