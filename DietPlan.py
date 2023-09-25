import pandas as pd

from pdfquery import PDFQuery

pdf = PDFQuery(r'C:\Users\Dani\Desktop\Python\Diet_plan\PDF\Dieta lekkostrawna SanDiet _ 1600 kcal (tydzień 1).pdf')
pdf.load()

# Use CSS-like selectors to locate the elements
text_elements = pdf.pq('LTTextLineHorizontal')

# Extract the text from the elements
text = [t.text for t in text_elements]

print(text)