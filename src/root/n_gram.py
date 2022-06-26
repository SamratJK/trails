import nltk
from nltk.corpus import stopwords
import string

string.punctuation
nltk.download("stopwords")

def remove_punctuation(text):
    # Defining the function to remove punctuation
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


def get_words(sentence):
    words = [
        word
        for word in sentence.split(" ")
        if word not in set(stopwords.words("english")) and word != ""
    ]

    return words


def generate_n_gram(sentence, city=None):

    sentence = remove_punctuation(sentence)
    words = get_words(sentence)
    if city:
        get_name = city.split(" ")
        for name in get_name:
            if name in words:
                words.remove(name)

    return [words, get_ngrams(words, 2), get_ngrams(words, 3)]
