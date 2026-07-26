import fitz  # pymupdf
import docx

# Read PDF CV
print('=== CV (PDF) ===')
doc = fitz.open('AJAY ARAVINDAN.pdf')
for page in doc:
    print(page.get_text())

print()
print('=== JOB DESCRIPTION (DOCX) ===')
jd = docx.Document('Junior Content Services Technician Job description.docx')
for para in jd.paragraphs:
    if para.text.strip():
        print(para.text)
