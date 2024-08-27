# https://pypdf.readthedocs.io/en/latest/

# run python3 pdf_merger.py dummy.pdf twopage.pdf wtr.pdf
import sys
from pypdf import PdfWriter

inputs = sys.argv[1:]

# merge pdf files
def pdf_merger(pdf_list):
    merger = PdfWriter()

    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("merged-pdf.pdf")
    merger.close()

pdf_merger(inputs)

    