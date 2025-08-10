import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

def analyze(sentence):
    doc = nlp(sentence)
    print(f"\nAnalysis of: \"{sentence}\"")
    print(f"{'Word':<15}{'POS':<10}{'Base Form':<15}")
    print("-" * 40)
    for token in doc:
        print(f"{token.text:<15}{token.pos_:<10}{token.lemma_:<15}")

# Main Program
if __name__ == "__main__":
    while True:
        text = input("\nEnter a sentence (or type 'quit' to exit): ")
        if text.lower() == "quit":
            break
        analyze(text)
