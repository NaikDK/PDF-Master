from PyPDF2 import PdfWriter, PdfReader
from tkinter import *

from Controller.GenericController import GenericController

class MergeController(GenericController):
    def __init__(self):
        super().__init__()
        self.files = []
        self.final = PdfWriter()

    def add_pdf(self):
        files = super().select_pdfs()
        self.files.append(files)

    def merge_files(self):
        for file in self.files:
            file_content = PdfReader(file, 'rb')
            for page in file_content.pages:
                self.final.add_page(page)

    def downlaod_merged(self):
        file = super().get_download_location()
        with open(file, "wb") as f:
            self.final.write(f)