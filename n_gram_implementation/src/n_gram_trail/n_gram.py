import nltk
from nltk.corpus import stopwords
import string
string.punctuation
nltk.download("stopwords")
#defining the function to remove punctuation
def remove_punctuation(text):
  if(type(text)==float):
    return text
  ans=""  
  for i in text:     
    if i not in string.punctuation:
      ans+=i    
  return ans


def generate_n_gram(sentence, ngrams=1):
    n_grams = list()
    sentence = remove_punctuation(sentence)
    words = [
        word
        for word in sentence.split(" ")
        if word not in set(stopwords.words("english")) and word != ''
    ]
    

    if ngrams == 1:
        return words
    else:

        for index in range(0, len(words) - 1):
            if index + ngrams == len(words) - 1:
                break
            word = " ".join(words[index : index + ngrams])
            n_grams.append(word)
        return n_grams
