# write a program to manipulate pdf files using pyPDF.
# Your programs should be able to marge multiple pdf files into a single pdf.
# you are welcome to add more functionalities
# pypdf is a free and open-source pure-python PDF library capable of splitting, merging, cropping,
# and transforming the pages of pdf files.
# It also add custom data, viewing options, and passwords to pdf files
# pypdf can retrieve text and metadata from pdfs as well.

from PyPDF2 import PdfWriter
import os

# Specify the folder containing the PDF files
folder_path = "pdf_folder"

# Get the list of files in the folder
files = os.listdir(folder_path)

# Initialize a list to store PDF file paths
pdf_files = []

# Filter for PDF files
for file in files:
    if file.endswith(".pdf"):
        pdf_files.append(os.path.join(folder_path, file))  # Use full file paths

# Create a PdfWriter instance
merger = PdfWriter()

# Merge the PDF files
for pdf_file in pdf_files:
    merger.append(pdf_file)

# Write the merged PDF to a new file
output_file = "merged-pdf.pdf"
merger.write(output_file)
merger.close()

print(f"Merged PDF saved as '{output_file}'.")
