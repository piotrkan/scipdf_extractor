import os
from pypdf import PdfReader

def change_pdf_files(path)-> None:
    """
    	Function for renaming supplied pdf files to more
        programming-friendly way (removing whitespace). 
        Note: pdfs present in github were already processed using this
        function
    Args:
    	path - path to the pdf dir
    """
    pdf_list = os.listdir(path)
    for pdf in pdf_list:
        if pdf.endswith('.pdf'):
            new_name = pdf.replace(' ', '_').lower()
            old_path = os.path.join(path, pdf)
            new_path = os.path.join(path, new_name)
            os.rename(old_path, new_path)
    
def extract_txt_from_pdf(path:str) -> str:
    """
    	Function for extracting text from pdf. NOTE: needs testing
        and more controlled text extraction (at the moment ALL text getting extracted)
    Args:
    	path - path to the pdf to be read
	Outs:
	    the extracted text in str format
    """
    reader = PdfReader(path)
    number_of_pages = len(reader.pages)
    page_texts = []
    for i in range(1,number_of_pages):
        page = reader.pages[i]
        text = page.extract_text()
        page_texts.append(text)
    return ''.join(page_texts)

def main():
    change_pdf_files('data')
    
if __name__=='__main__':
    main()