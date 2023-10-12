import sys
from pypdf import PdfReader, PdfWriter

# run python3 pdf_add_watermark.py 
# run python3 pdf_remove_watermark.py add_watermark.pdf

original_pdf = sys.argv[1]
with open(original_pdf, "rb") as input_file, open('remove_watermark.pdf', "wb") as output_file:

    reader = PdfReader(input_file)
    writer = PdfWriter()

    for n in range(len(reader.pages)):

        page = reader.pages[n]
        del page["/Contents"][0]

        writer.add_page(page)

    writer.write(output_file)