import nltk
from nltk.util import ngrams

# Input sentence and n value
sentence = "Python provides powerful tools for language processing"
n = 4

# -------- Word n-grams --------
words = sentence.split()
word_ngrams = ngrams(words, n)

print("Word", n, "-grams:")
for gram in word_ngrams:
    print(gram)

print("\nCharacter", n, "-grams:")

# -------- Character n-grams --------
char_ngrams = ngrams(sentence, n)

for gram in char_ngrams:
    print("".join(gram))
