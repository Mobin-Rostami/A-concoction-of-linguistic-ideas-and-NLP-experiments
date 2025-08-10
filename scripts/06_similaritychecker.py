import spacy
nlp = spacy.load("en_core_web_sm")

doc1 = nlp("I like to play football.")
doc2 = nlp("I enjoy playing soccer.")

print("Similarity:", doc1.similarity(doc2))
