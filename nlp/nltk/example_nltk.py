import nltk
nltk.download("punkt", quiet=True)
from nltk.tokenize import word_tokenize
print(word_tokenize("שלום עולם, NLP with NLTK is simple."))
