import fitz
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
      text += page.get_text()
    return text
sustainability_text = extract_text_from_pdf("report.pdf")
print(sustainability_text[:500])