'''gradio app script'''
import os
import json
import gradio as gr
from src import data, model

def pdf_ext_wrapper(input_pdf:str)->dict:
    """
    	Wrapper for extracting entities from pdfs for gradio
    Args:
    	input_pdf - path to the pdf to be read
	Outs:
	    json file with extracted entities
    """
    output= data.extract_txt_from_pdf(input_pdf)
    output = model.extract_entities_with_context('en_ner_bc5cdr_md', output)
    return json.dumps(output)

def main():
    #define interace and launch
    demo = gr.Interface(
        fn=pdf_ext_wrapper,
        inputs=["file"],
        outputs=[gr.JSON(label='Json output')],
        examples = [os.path.join('data',pdf) for pdf in os.listdir('data')],
        title = 'SciPDF NER extractor',
        description = 'Prototype of NER extractor from scientific papers in PDF format',
                        )
    demo.launch(show_error=True )

if __name__=='__main__':
    main()
