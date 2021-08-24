from decimal import ROUND_DOWN
from os import stat_result
import tkinter as tk
from tkinter import filedialog
from tkinter.constants import ACTIVE, ANCHOR, DISABLED
from typing import Text
from PyPDF2 import PdfFileWriter, PdfFileReader

filepath1 = ""
filename1 = ""
filepath2 = ""
filename2 = ""
output = PdfFileWriter()

def radio_change():
    global v, Deletor, Merger, Splitter
    if(v.get() == "2"):
        Deletor.grid_forget()
        Splitter.grid_forget()
        Merger.grid(row=1, column=0, columnspan=3, sticky=tk.W, padx="45")
    elif(v.get() == "1"):
        Merger.grid_forget()
        Splitter.grid_forget()
        Deletor.grid(row=1, column=0, columnspan=3, sticky=tk.W, padx="45")
    elif(v.get() == "3"):
        Merger.grid_forget()
        Deletor.grid_forget()
        Splitter.grid(row=1, column=0, columnspan=3, sticky=tk.W, padx="45")

def select_pdf():
    global filepath1, filename1, filepath2, filename2, status_var
    file = filedialog.askopenfilename(title="Select PDF")
    if(filename1 == ""):
        filename1 = file[file.rfind("/")+1:]
        filepath1 = file[:file.rfind("/")+1]
        status_var.set("Status: File selected: " + filename1)
    else:
        filename2 = file[file.rfind("/")+1:]
        filepath2 = file[:file.rfind("/")+1]
        status_var.set("Status: File selected: " + filename2)

def select_pdf_to_truncate():
    global In_selector, deleted_file
    select_pdf()
    In_selector.configure(state=DISABLED)
    deleted_file.configure(state=ACTIVE)

def delete_pages():
    global filename1, filepath1, pages_delete, download, output, status_var
    infile = PdfFileReader(filepath1+filename1, 'rb')
    output = PdfFileWriter()
    pages_to_delete = pages_delete.get().split(",")
    for i in range (0, infile.getNumPages()):
        if(str(i+1) not in pages_to_delete):
            p = infile.getPage(i)
            output.addPage(p)
    pages_delete.set("")
    download.configure(state=ACTIVE)
    status_var.set("Status: " + str(len(pages_to_delete)) + " Page(s) deleted")

def download_new_pdf():
    global filepath1, filename1, output, In_selector
    new_path = filepath1 + "converted_" + filename1
    with open(new_path, 'wb') as f:
        output.write(f)
    In_selector.configure(state=ACTIVE)
    status_var.set("Status: converted_" + filename1 + " downloaded!")

def select_pdf1_to_merge():
    global In_file2, In_file1
    select_pdf()
    In_file2.configure(state=ACTIVE)
    In_file1.configure(state=DISABLED)

def select_pdf2_to_merge():
    global In_file2
    select_pdf()
    In_file2.configure(state=ACTIVE)
    merge.configure(state=ACTIVE)

def combine_files():
    global filename1, filename2, filepath1, filepath2, output, status_var
    output = PdfFileWriter()
    infile1 = PdfFileReader(filepath1+filename1, 'rb')
    infile2 = PdfFileReader(filepath2+filename2, 'rb')
    pages1 = infile1.getNumPages()
    for i in range(0, pages1):
        p = infile1.getPage(i)
        output.addPage(p)
    pages2 = infile2.getNumPages()
    for i in range(0, pages2):
        p = infile2.getPage(i)
        output.addPage(p)
    status_var.set("Status: " + str(pages1 + pages2) + " Page(s) Merged!!!")

def select_pdf_to_split():
    # print("Splitter...")
    global input_File, filename1, status_var
    select_pdf()
    input_File.configure(state=DISABLED)
    status_var.set("Status: File " + filename1 + "Selected.")

def split_selected():
    print("Splitter...")
    global filename1, filepath1, output, split
    infile = PdfFileReader(filepath1+filename1, 'rb')
    pages = infile.getNumPages()
    for i in range(0, pages):
        if i%int(split) == 0:
            new_path = filepath1 + "Split_" + filename1 + "_" + i%int(split)
            with open(new_path, 'wb') as f:
                output.write(f) # Remainig

def download_merged_pdf():
    global filepath1, filename1, filepath2, filename2, output
    new_path = filepath1 + "Merged_" + filename1 + "_" + filename2
    with open(new_path, 'wb') as f:
        output.write(f)
    status_var.set("Status: Merged_" + filename1 + "_" + filename2 + " downloaded!")

root = tk.Tk()
root.title("Page Deletor")
root.configure(background="lavender")

# Radiobutton declaration
v = tk.StringVar()
merge_files = tk.Radiobutton(root, text="Merge PDF Files", value="2", variable=v, command=radio_change, background="lavender")
delete_pdf_pages = tk.Radiobutton(root, text="Delete PDF Pages", value="1", variable=v, command=radio_change, background="lavender")
split_pdf = tk.Radiobutton(root, text="Split PDF", value="3", variable=v, command=radio_change, background="lavender")
v.set("2")

# Radiobuttons placement
merge_files.grid(row=0, column=0, padx=5, pady=5)
delete_pdf_pages.grid(row=0, column=1, padx=5, pady=5)
split_pdf.grid(row=0, column = 2, padx=5, pady=5)

# Deletor widget declaration Starts Here
Deletor = tk.Frame(root, name="deletor", background="lavender")
In_label = tk.Label(Deletor, text="Select input PDF: ", width="30", anchor="w", background="lavender")
In_selector = tk.Button(Deletor, text="Select PDF", command=select_pdf_to_truncate)
pages_delete = tk.StringVar()
delete_label = tk.Label(Deletor, width="30", text="Pages to be deleted(, separated)", anchor="w", background="lavender")
pages_to_be_deleted = tk.Entry(Deletor, width="20", textvariable=pages_delete, background="misty rose")
deleted_file = tk.Button(Deletor, text="Delete Pages", command=delete_pages, state=DISABLED)
download = tk.Button(Deletor, text=("Download file"), command=download_new_pdf, state=DISABLED)

# Deletor widget placement Starts Here
In_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
In_selector.grid(row=0, column=1, padx=5, pady=5)
delete_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
pages_to_be_deleted.grid(row=1, column=1, padx=5, pady=5)
deleted_file.grid(row=2, column=0, padx=5, pady=5)
download.grid(row=2, column=1)

#Merger widget declaration Starts Here
Merger = tk.Frame(root, name="merger", background="lavender", width=30)
In_file1_label = tk.Label(Merger, text="Select input PDF1: ", width="30", anchor="w", background="lavender")
In_file1 = tk.Button(Merger, text="Select PDF", command=select_pdf1_to_merge)
In_file2_label = tk.Label(Merger, text="Select input PDF2: ", width="30", anchor="w", background="lavender")
In_file2 = tk.Button(Merger, text="Select PDF", command=select_pdf2_to_merge, state=DISABLED)
merge = tk.Button(Merger, text="Merge Files", command=combine_files, state=DISABLED)
download_merged = tk.Button(Merger, text="Download", command=download_merged_pdf)

# Merger widget placement
Merger.grid(row=1, column=0, columnspan=3, sticky=tk.W, padx="50")
In_file1_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
In_file1.grid(row=0, column=1, padx=5, pady=5, )
In_file2_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
In_file2.grid(row=1, column=1, padx=5, pady=5)
merge.grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
download_merged.grid(row=2, column=1, padx=5, pady=5)

# Split widget declaration
Splitter = tk.Frame(root, name="splitter", background="lavender", width="45")
input_File_Label = tk.Label(Splitter, text="Select PDF File", width="15", background="lavender", anchor="w")
input_File = tk.Button(Splitter, text="Select PDF", command=select_pdf_to_split)
split_Size_Label = tk.Label(Splitter, text="Enter split page size: ", width="30", background="lavender", anchor="w")
split = tk.StringVar()
split_Size = tk.Entry(Splitter, textvariable=split, width="20", background="misty rose")
split_Button = tk.Button(Splitter, text="Split File", command=split_pdf)

# Split widget placement
input_File_Label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
input_File.grid(row=0, column=1, padx=5, pady=5)
split_Size_Label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
split_Size.grid(row=1, column=1, padx=5, pady=5)
split_Button.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

# Status bar
status_var = tk.StringVar()
status = tk.Label(root, textvariable=status_var, width="60", anchor="w", background="lavender")
status_var.set("Status: ")
status.grid(row=2, columnspan=3, padx=15, pady=5, sticky=tk.W)

# Author Line
Author_line = tk.Label(root, text="Produced by: Deep Naik", background="lavender", fg="gray30")
Author_line.grid(row=5, column=0, columnspan=3)
root.mainloop()