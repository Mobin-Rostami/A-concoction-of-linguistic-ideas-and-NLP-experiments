import spacy
nlp = spacy.load("en_core_web_sm")

def highlight_entities(text):
    doc = nlp(text)
    for ent in doc.ents:
        print(f"{ent.text:<25}  {ent.label_}")

text = "Barack Obama was born in Hawaii and served as the 44th President of the United States."
highlight_entities(text)
