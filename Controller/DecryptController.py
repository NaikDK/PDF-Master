from PyPDF2 import PdfWriter, PdfReader
from tkinter import *

from Controller.GenericController import GenericController


class DecryptController(GenericController):
    def __init__(self):
        super().__init__()
        self.files = []
        self.final = PdfWriter()

    def add_pdf(self):
        files = super().select_pdfs()
        for file in files:
            self.files.append(file)    