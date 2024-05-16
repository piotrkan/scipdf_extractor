import spacy

def extract_entity_context(doc, entity_text:str, span_length:int)  -> str:
    """
    	Function for extracting context for specific entities
    Args:
    	doc - spacy doc object containing entities
        entity_text - entity for which context is sought for
        span_length - the context window, specifying no. tokens before & after entity keyword
	Outs:
	    the extracted context for entity in str format
    """
    #loop through provided entities
    for ent in doc.ents:
        if ent.text == entity_text:
            start_token = max(ent.start - span_length, 0) #index starting context
            end_token = min(ent.end + span_length, len(doc)) #index ending context
            context_tokens = doc[start_token:end_token]
            return context_tokens.text, start_token, end_token

def extract_entities_with_context(model, text:str, span_length:int=10) -> list:
    """
    	Function for extracting entities from provides strings
    Args:
    	model - ner model from spacy for entity extraction
        text - corpus of the pdf 
        span_length - optional, the context window, specifying no. tokens before & after entity keyword
	Outs:
	    list of dictionaries containing entity, location and context
    """
    #load the ner model and apply it to the text
    nlp = spacy.load(model) 
    doc = nlp(text)
    
    # Extract entities and their labels
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # extract entities and context
    entities_with_context = []
    for ent in doc.ents:
        context, start, end = extract_entity_context(doc, ent.text, span_length)
        entities_with_context.append({
            'entity': ent.text, #entity
            'start':start, #start token 
            'end': end, #end token
            # 'label': ent.label, #label, not needed at the moment
            'context': context # specified context
        })
    print(entities_with_context)
    return entities_with_context