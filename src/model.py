import spacy

def extract_entity_context(doc, entity_text, span_length):
    for ent in doc.ents:
        if ent.text == entity_text:
            start_token = max(ent.start - span_length, 0)
            end_token = min(ent.end + span_length, len(doc))
            context_tokens = doc[start_token:end_token]
            return context_tokens.text

def extract_entities_with_context(model, text, span_length=10):
    nlp = spacy.load(model) 
    doc = nlp(text)
    # Process the text with SpaCy
    doc = nlp(text)
    
    # Extract entities and their labels
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # Extract and print context for each entity
    entities_with_context = []
    for entity, label in entities:
        context = extract_entity_context(doc, entity, span_length)
        entities_with_context.append({
            'entity': entity,
            'start':entity.start,
            'end': entity.end
            # 'label': label,
            'context': context
        })
    print(entities_with_context)
    return entities_with_context