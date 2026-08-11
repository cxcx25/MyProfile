from docx import Document

def read_docx_content(docx_path):
    doc = Document(docx_path)
    content = []
    for para in doc.paragraphs:
        if para.text.strip():
            content.append(para.text)
    return '\n'.join(content)

if __name__ == "__main__":
    docx_path = r"c:\Project\MyProfile\original-theme\Joseph Rey Marilla.docx"
    content = read_docx_content(docx_path)
    print(content)
