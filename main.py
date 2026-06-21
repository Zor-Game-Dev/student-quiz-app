import fitz

pdf = fitz.open("sample.pdf")

full_text = ""

for page in pdf:
    full_text += page.get_text()

print(full_text)