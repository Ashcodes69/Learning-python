from PyPDF2 import PdfWriter

# use this commmand in terminal pip install PyPDF2

import os

merger = PdfWriter()  # this function is provided by pyPDF2

for pdf in os.listdir("pdf_folder"):  # list all pdf files from a folder
    merger.append(
        os.path.join("pdf_folder", pdf)
    )  # passing the pdf files to PdfWriter function

merger.write(
    os.path.join("pdf_folder", "merged-pdf.pdf")
)  # merging those pdf files into one file
merger.close()
