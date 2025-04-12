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
    
    def decrypt_pdf(self, password):
        for file in self.files:
            try:
                file_obj = PdfReader(file)
                if file_obj.is_encrypted:
                    file_obj.decrypt(password)
                else:
                    print(f"{file} is not encrypted.")
                    raise ValueError("File is not encrypted.")
                for page in range(len(file_obj.pages)):
                    self.final.add_page(file_obj.pages[page])
            except ValueError as ve:
                return ValueError                
        return True

    def download_pdf(self):
        file = super().get_download_location()
        try:
            with open(file, "wb") as f:
                self.final.write(f)
            self.final = PdfWriter()
            self.files = []
            return True
        except Exception as e:
            print("Error: ", e)
            return False