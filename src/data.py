import os
import pymupdf

def change_pdf_files(path:str)-> None:
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
    
def extract_txt_from_pdf(path:str, pages:list=None) -> str:
    """
    	Function for extracting text from pdf. NOTE: needs testing
        and more controlled text extraction (at the moment ALL text getting extracted)
    Args:
    	path - path to the pdf to be read
        pages - optional, list of pages to be read
	Outs:
	    the extracted text in str format
    """
    doc = pymupdf.open(path)
    print(type(doc))
    number_of_pages = doc.page_count
    page_texts = []
    if pages==None:
        for i in range(number_of_pages):
            page = doc[i]
            text = page.get_text()
            page_texts.append(text)
    else:
        for i in pages:
            page = doc.pages[i]
            text = page.get_text()
            page_texts.append(text)
    return ''.join(page_texts)

def main():
    change_pdf_files('data')
    
if __name__=='__main__':
    main()