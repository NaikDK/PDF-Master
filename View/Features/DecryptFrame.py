from tkinter import *
from tkinter import messagebox

class DecryptFrame(Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(background="lavender")
        self.create_widgets()

    def create_widgets(self):
        # Create widgets for the DecryptFrame

        self.select_pdf_label = Label(self, text="Select PDF to decrypt:", anchor="w")
        self.select_pdf = Button(self, text="Select PDF", command=self.add_file)

        self.selected_files_label = Label(self, text="Selected PDFs", width="30", anchor="w")
        self.selected_pdfs = Listbox(
            self, width=30, height=1, background="lavender", fg="gray30", selectmode=SINGLE
        )

        self.password_label = Label(self, text="Enter password", anchor="w")
        self.password = Entry(self, show="*", width=20, background="misty rose")

        self.decrypt = Button(self, text="Decrypt PDF", command=self.decrypt_pdf, state=DISABLED)
        # self.download_pdf = Button(self, text="Download PDF", command=self.download_pdf, state=DISABLED)

        # Place widgets in the frame

        self.select_pdf_label.grid(row=0, column=0, padx=5, pady=5)
        self.select_pdf.grid(row=0, column=1, padx=5, pady=5)
        self.selected_files_label.grid(row=1, column=0, padx=5, pady=5)
        self.selected_pdfs.grid(row=1, column=1, padx=5, pady=5)
        self.password_label.grid(row=2, column=0, padx=5, pady=5)
        self.password.grid(row=2, column=1, padx=5, pady=5)
        self.decrypt.grid(row=3, column=1, sticky=W, padx=5, pady=5)
        # self.download_pdf.grid(row=3, column=1, padx=5, pady=5)
        self.selected_pdfs.insert(END, "No files to decrypt")

    def add_file(self):
        self.controller.add_pdf()
        if self.controller.files:
            self.selected_pdfs.delete(0, END)
            files = list(self.controller.files)
            for file in files:
                self.selected_pdfs.insert(END, file)

        if len(self.selected_pdfs.get(0)) > 0:
            self.decrypt.config(state=ACTIVE)
    
    def decrypt_pdf(self):
        if self.password.get() == "":
            messagebox.showerror("Error", "Please enter a password")
        try:
            if self.controller.decrypt_pdf(self.password.get()):
                self.download_pdf()
        except ValueError:
            messagebox.showerror("Error", "File is not encrypted")
        self.reset_frame()

    def download_pdf(self):
        status = self.controller.download_pdf()
        if status:
            messagebox.showinfo("Success", "File decrypted successfully")
            self.reset_frame()
        else:
            messagebox.showerror("error", "Error downloading file.\n Please try again.")
            self.reset_frame()

    def reset_frame(self):
        self.selected_pdfs.delete(0, END)
        self.password.delete(0, END)
        self.decrypt.config(state=DISABLED)
        # self.download_pdf.config(state=DISABLED)