import PyPDF2

def extract_page_from_pdf(pdf_path, page_number):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)

        if page_number < 0 or page_number >= len(reader.pages):
            raise ValueError(f"Invalid page number. The PDF has {reader.numPages} pages.")

        page = reader.pages[page_number]
        text = page.extract_text()

    return text

# Usage example
pdf_path = r'C:\Users\Dani\Desktop\Python\Diet_plan\PDF\Dieta lekkostrawna SanDiet _ 1600 kcal (tydzień 1).pdf'
page_number = 2  # Replace with the page number you want (0-indexed)

extracted_text = extract_page_from_pdf(pdf_path, page_number)
print(extracted_text)