import gradio as gr
from src import data, model
from pypdf import PdfReader
import os, json

def pdf_wrapper(input_pdf):
    output= data.extract_txt_from_pdf(input_pdf)
    output = model.extract_entities_with_context('en_ner_bc5cdr_md', output)
    return json.dumps(output)

def main():
    demo = gr.Interface(
        fn=pdf_wrapper,
        inputs=["file"],
        outputs=[gr.JSON(label='Json output')],
        examples = ['data/1.pdf', 'data/2.pdf','data/3.pdf'],
        title = 'SciPDF NER extractor',
        description = 'Prototype of NER extractor from scientific papers in PDF format',
                        )
    demo.launch()
    
if __name__=='__main__':
    main()