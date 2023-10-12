# https://pypdf.readthedocs.io/en/latest/

from pypdf import PdfReader, PdfWriter

# rotate pdf file
reader = PdfReader("dummy.pdf")
page = reader.pages[0]
page.rotate(270)
writer = PdfWriter()
writer.add_page(page)
writer.write('tilt.pdf')
