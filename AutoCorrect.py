import re
from collections import Counter


def words(text):
    return re.findall(r'\w+', text.lower())


CorpusFile = open('Corpus.txt').read()
WORDS = Counter(words(CorpusFile))


def Prob(word, N=sum(WORDS.values())):
    # Probability of word.
    return WORDS[word] / N


def correction(word):
    # Most probable spelling correction for word.

    return max(correctwords(word), key=Prob)


def correctwords(word):
    # All possible spelling corrections for word.
    return knownword([word]) or knownword(editDistance1(word)) or knownword(editDistance2(word)) or [word]


def knownword(words):
    # The subset of words that appear in the dictionary of WORDS.
    return set(w for w in words if w in WORDS)


def editDistance1(word):
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    # Remove any one character from the word.
    Removeonechar = [(word[:i] + word[i + 1:]) for i in range(len(word))]
    # Adding one character any where in the word.
    InsertOneChar = [(word[:i] + c + word[i:]) for i in range(len(word) + 1) for c in alphabets]
    # Transposing the order of any two adjacent characters.
    Transpose = [word[:i] + word[i + 1:i + 2] + word[i:i + 1] + word[i + 2:] for i in range(len(word) - 1)]
    # Substituting any character in the word with another character.
    Replacing = [(word[:i] + c + word[i + 1:]) for i in range(len(word)) for c in alphabets]
    return set(Removeonechar + InsertOneChar + Transpose + Replacing)


def editDistance2(word):
    return (editDis2 for editDis1 in editDistance1(word) for editDis2 in editDistance1(editDis1))



