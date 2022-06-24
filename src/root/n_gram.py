import nltk
from nltk.corpus import stopwords
import string

string.punctuation
nltk.download("stopwords")
# defining the function to remove punctuation
def remove_punctuation(text):
    if type(text) == float:
        return text
    ans = ""
    for i in text:
        if i not in string.punctuation:
            ans += i
    return ans


def get_ngrams(words, ngrams):
    n_grams = list()

    for index in range(0, len(words) - 1):

        if index + ngrams > len(words):
            break
        word = " ".join(words[index : index + ngrams])
        n_grams.append(word)

    return n_grams


def generate_n_gram(sentence):

    sentence = remove_punctuation(sentence)
    words = [
        word
        for word in sentence.split(" ")
        if word not in set(stopwords.words("english")) and word != ""
    ]
    return [words, get_ngrams(words, 2), get_ngrams(words, 3)]
