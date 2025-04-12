from PyPDF2 import PdfWriter, PdfReader
from tkinter import *

from Controller.GenericController import GenericController

class SplitController(GenericController):
    def __init__(self):
        super().__init__()
        self.files = []
        self.final = PdfWriter()