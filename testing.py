import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
from nltk.tag import pos_tag

def process_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Part-of-Speech (POS) tagging
    pos_tags = pos_tag(tokens)
    
    return tokens, pos_tags

# Example usage
text = "Open a website and fetch my details."
tokens, pos_tags = process_text(text)
print(f"Tokens: {tokens}")
print(f"POS Tags: {pos_tags}")
