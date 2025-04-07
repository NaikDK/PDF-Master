class DeletePagesFrame:
    def __init__(self, parent, processor):
        super().__init__(parent)
        self.processor = processor
        self.label = tk.Label(self, text="Delete Pages", font=("Arial", 14))