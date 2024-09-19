from pypdf import PdfReader, PdfWriter

reader = PdfReader("health_report.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

for page in writer.pages:
    for img in page.images:
        img.replace(img.image, quality=15)

with open("health_report_edited.pdf", "wb") as f:
    writer.write(f)