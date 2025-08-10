import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def add_warning_clause(text):
    """
    Find 'ISIS' (any case) in text and add a warning phrase right after it.
    """
    words = text.split()
    new_words = []
    for w in words:
        # Check if the word is 'ISIS' ignoring case
        if w.lower() == "isis":
            # Add the adjective clause right after the word
            new_words.append(w)
            new_words.append(", which is a violent, dangerous, criminal terrorist organization")
        else:
            new_words.append(w)
    # Join the words back into a string
    return " ".join(new_words)

def show_entities(text):
    """
    Print named entities found in the text.
    """
    doc = nlp(text)
    for ent in doc.ents:
        print(f"{ent.text:<20} {ent.label_}")

# Example
original_text = "ISIS claimed responsibility for the attack."

print("Original text:")
print(original_text)

modified_text = add_warning_clause(original_text)

print("\nModified text:")
print(modified_text)

print("\nNamed entities:")
show_entities(modified_text)
