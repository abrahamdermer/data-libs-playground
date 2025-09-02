import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("ChatGPT from OpenAI works in 2025.")
for ent in doc.ents:
    print(ent.text, ent.label_)
