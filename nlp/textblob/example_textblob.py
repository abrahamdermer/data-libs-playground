from textblob import TextBlob
tb = TextBlob("I love Python!")
print("Polarity, subjectivity:", tb.sentiment)
