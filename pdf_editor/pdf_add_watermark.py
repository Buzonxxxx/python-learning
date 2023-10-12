# https://pypdf.readthedocs.io/en/latest/

from pypdf import PdfWriter, PdfReader

watermark = PdfReader("wtr.pdf").pages[0]
writer = PdfWriter(clone_from="twopage.pdf")
for page in writer.pages:
    page.merge_page(watermark, over=False)  # here set to False for watermarking

writer.write("add_watermark.pdf")

    