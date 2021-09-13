import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText)

print(getText('abrir.docx'))

# Ignora las imagenes en caso de que contenga en lugar de lenvantar error
