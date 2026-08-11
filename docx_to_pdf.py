from docx2pdf import convert

def docx_to_pdf(docx_path, pdf_path):
    convert(docx_path, pdf_path)
    print(f"Successfully created {pdf_path}")

if __name__ == "__main__":
    docx_path = r"c:\Project\MyProfile\original-theme\Joseph Rey Marilla_updated.docx"
    pdf_path = r"c:\Project\MyProfile\Joseph_Rey_Marilla_CV.pdf"
    docx_to_pdf(docx_path, pdf_path)
