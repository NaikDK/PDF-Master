class UIHelper:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Master")
        self.root.configure(background="lavender")
        self.processor = PDFProcessor()
        self.create_widgets()

    def create_widgets():
        pass

    