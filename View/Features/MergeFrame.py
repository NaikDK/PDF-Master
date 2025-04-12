from tkinter import *

class MergeFrame(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background="lavender")
        self.controller = controller
        self.files = []
        self.create_merge_widgets()
    
    def create_merge_widgets(self):
        In_file1_label = Label(
            self, text="Select input PDF1: ", width="30", anchor="w", background="lavender", fg="gray30"
        )
        In_file1 = Button(self, text="Select PDFs", command=self.add_files)

        selected_files_label = Label(self, text="Selected PDFs", width="30", anchor="w", background="lavender")
        self.selected_pdfs = Listbox(
            self, width=30, background="lavender", fg="gray30", selectmode=SINGLE
        )
        self.merge = Button(self, text="Merge Files", command=self.combine_files, state=DISABLED)
        self.download_merged = Button(self, text="Download", command=self.download_merged_pdf, state=DISABLED)

        In_file1_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)
        In_file1.grid(row=0,column=1,padx=5,pady=5,)
        selected_files_label.grid(row=1, column = 0, padx=5, pady=5)
        self.selected_pdfs.grid(row=1, column=1, padx=5, pady=5)
        self.merge.grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.download_merged.grid(row=2, column=1, padx=5, pady=5)
        self.selected_pdfs.insert(END, "No files to merge")

    def add_files(self):
        self.controller.add_pdf()
        if self.controller.files:
            self.selected_pdfs.delete(0, END)
            files = list(self.controller.files)
            for file in files:
                self.selected_pdfs.insert(END, file)

        if len(self.selected_pdfs.get(0)) > 0:
            self.merge.config(state=ACTIVE)

    def combine_files(self):
        success = self.controller.merge_files()
        if success:
            self.download_merged.config(state=ACTIVE)
            self.selected_pdfs.delete(0, END)
            self.selected_pdfs.insert(END, "Files Merged Successfully")
        else:
            self.selected_pdfs.delete(0, END)
            self.selected_pdfs.insert(END, "No files to merge")

    def download_merged_pdf(self):
        status = self.controller.downlaod_merged()
        if status:
            self.selected_pdfs.delete(0, END)
            self.selected_pdfs.insert(END, "Files Downloaded Successfully")
            self.download_merged.config(state=DISABLED)
        else:
            self.selected_pdfs.delete(0, END)
            self.selected_pdfs.insert(END, "Error in downloading files")
        