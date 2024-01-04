import pandas as pd

def keep_first_two_words(sentence):
    words = sentence.split()
    return ' '.join(words[:2])
