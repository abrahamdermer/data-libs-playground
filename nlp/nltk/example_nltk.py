import nltk
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True) 
nltk.download("averaged_perceptron_tagger", quiet=True)
nltk.download("wordnet", quiet=True)

try:
    nltk.download("averaged_perceptron_tagger_eng", quiet=True)
except:
    pass
try:
    nltk.download("averaged_perceptron_tagger", quiet=True)
except:
    pass

from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk import pos_tag

text = "Dogs are running faster than the other animals."

# Tokenization
tokens = word_tokenize(text)
print("Tokens:", tokens)

# POS Tagging (זיהוי תפקיד תחבירי: שם עצם, פועל וכו')
tags = pos_tag(tokens)
print("POS Tags:", tags)

# Stemming (קיצוץ למקור בסיסי)
stemmer = PorterStemmer()
stems = [stemmer.stem(word) for word in tokens]
print("Stems:", stems)

# Lemmatization (צורה בסיסית "חוקית")
lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(word) for word in tokens]
print("Lemmas:", lemmas)
