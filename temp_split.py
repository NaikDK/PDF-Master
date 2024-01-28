from PyPDF2 import PdfFileWriter, PdfFileReader

output = PdfFileWriter()
filepath = "D:\\Books\\Cambridge Books\\Cambridge 16\\Cambridge IELTS_16_academic[@cambridgematerials].pdf"
infile = PdfFileReader(filepath, 'rb')

start_page = int(input("Start Page: "))
no_of_pages = int(input("Number of pages: "))

for i in range(start_page, start_page+no_of_pages):
    p = infile.getPage(i)
    output.addPage(p)

output_filename = input("Target file name: ")
target = "D:\\Books\\Cambridge Books\\Cambridge 16\\" + output_filename + ".pdf"
with open(target, 'wb') as f:
    output.write(f)