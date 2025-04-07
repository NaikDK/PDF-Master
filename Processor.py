from tkinter import filedialog


class Processor:
    def __init__(self):
        self.files = []

    @staticmethod
    def add_pdf(self, filepath):
        file = filedialog.askopenfilename(title="Select PDF", filetypes=[("PDF Files", "*.pdf")])
        if file:
            self.files.append(file)

    def Merge_PDFs(self):
        pass

    def delete_pages(self):
        pass

    def split_PDF(self):
        pass

    def sub_PDF(self):
        pass