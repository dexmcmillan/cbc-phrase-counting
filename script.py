from nltk import ngrams
from collections import Counter
import pandas as pd
import string

# A small function that will convert a tuple to a string.
def convertTuple(tup):
    str = ' '.join(tup)
    return str

# This will read in the text to be processed from a file in the project's root folder called "text.txt"
with open('cbc-phrase-counting/text.txt', 'r') as file:
    sentence = file.read().rstrip().translate(str.maketrans('', '', string.punctuation)).lower()

# This is the number of words in each phrase to be counted.
n = 3

# An empty list to collect all of the phrases for counting.
all_bigrams = []

# The ngrams function processes the text and the loop pushes each phrase to the empty list we created.
bigrams = ngrams(sentence.split(), n)
for gram in bigrams:
    all_bigrams.append(convertTuple(gram))

# Our phrase counts in a list.
phrase_counts = Counter(all_bigrams)

# Put into a Pandas dataframe.
df = pd.DataFrame(phrase_counts, index=["Count"]).transpose().sort_values(by="Count", ascending=False)
print(df)
df.to_clipboard()