from PyPDF2 import PdfWriter, PdfReader

class MergeFrame:
    def __init__(self):
        self.files = []

    def add_pdf(self, file):
        self.files.append(file)

    def merge_files(self, pdf1):
        output = PdfWriter()
        for file in self.files:
            file_content = PdfReader(file, 'rb')
            for page in file_content.pages:
                output.add_page(page)
