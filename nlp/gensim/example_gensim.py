from gensim.models import Word2Vec
sentences = [["data","science","is","fun"],["nlp","with","gensim"]]
model = Word2Vec(sentences, vector_size=50, min_count=1, epochs=100)
print("Vector for 'data' (first 5):", model.wv["data"][:5])
