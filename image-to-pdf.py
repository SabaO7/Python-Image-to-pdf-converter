import img2pdf

with open('test.png', 'rb') as f:
    img =f.read()
pdf_bytes = img2pdf.convert(img)


with open('output.pdf', 'wb') as f:
    f.write(pdf_bytes)