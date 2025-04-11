from tkinter import filedialog

class GenericController():
    def __init__(self):
        pass
        
    def select_pdfs(self):
        files = filedialog.askopenfilenames(
            title="Select PDF files",
            filetypes=[("PDF files", "*.pdf")],
        )
        return files

    def get_download_location(self):
        file = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF files", "*.pdf")],
        )
        return file