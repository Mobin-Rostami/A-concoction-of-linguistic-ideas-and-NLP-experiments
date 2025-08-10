import spacy
nlp = spacy.load("en_core_web_sm")

text = "The striped cats were chasing mice."
doc = nlp(text)

for token in doc:
    print(f"{token.text:<15}{token.lemma_}")

