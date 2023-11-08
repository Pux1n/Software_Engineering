import re

sentence = 'Hello, world! Python IS the programming language of thE future. My EMAIL is.... \nPYTHON is awesome!!!!'
with open('input.txt', 'r') as f:
    ban_words = f.readline().split()
    for word in ban_words:
        sentence = re.sub(word, len(word)*'*', sentence, flags=re.IGNORECASE)
print(sentence)
