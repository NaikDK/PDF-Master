from tkinter import *

class MergeFrame(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background="lavender")
        self.controller = controller
        # self.pack(fill="both", expand=True)
        self.files = []
        self.create_merge_widgets()
    
    def create_merge_widgets(self):
        In_file1_label = Label(
            self, text="Select input PDF1: ", width="30", anchor="w", background="lavender", fg="gray30"
        )
        In_file1 = Button(self, text="Select PDFs", command=self.add_files)
        # In_file2_label = Label(
        #     self, text="Select input PDF2: ", width="30", anchor="w", background="lavender", fg="gray30"
        # )
        # In_file2 = Button(
        #     self, text="Select PDF", command=self.add_pdf, state=DISABLED
        # )
        merge = Button(self, text="Merge Files", command=self.combine_files, state=DISABLED)
        download_merged = Button(self, text="Download", command=self.download_merged_pdf, state=DISABLED)

        In_file1_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        In_file1.grid(
            row=0,
            column=1,
            padx=5,
            pady=5,
        )
        # In_file2_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
        # In_file2.grid(row=1, column=1, padx=5, pady=5)
        merge.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        download_merged.grid(row=2, column=1, padx=5, pady=5)

    def add_files(self):
        self.controller.add_pdf()

    def combine_files(self):
        self.controller.merge_files(self.files)

    def download_merged_pdf(self):
        self.controller.downlaod_merged()