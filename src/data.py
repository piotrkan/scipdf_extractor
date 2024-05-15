from pypdf import PdfReader
import os
import re
import json
    
def extract_txt_from_pdf(path) -> list:
    reader = PdfReader(path)
    number_of_pages = len(reader.pages)
    page_texts = []
    for i in range(1,number_of_pages-1):
        page = reader.pages[i]
        text = page.extract_text()
        page_texts.append(text)
    return ''.join(page_texts)