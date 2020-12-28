import nltk
from nltk.corpus import stopwords
import unidecode
import string
import re


def minusculas(comment):
    return comment.lower()


def acentos_signos(comment):
    string.punctuation += '¡'
    reg_signos = re.compile('[%s]' % re.escape(string.punctuation))
    sin_signos = reg_signos.sub('', comment)
    return unidecode.unidecode(sin_signos)


def tokenizar(comment):
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    return tokenizer.tokenize(comment)


def eliminar_stop_words(comment):
    stop_words = set(stopwords.words('spanish'))
    filtered_sentence = [w for w in comment if not w in stop_words]
    filtered_sentence = []
    for w in comment:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence


def procesar_comentario(comment):

    lower_text = minusculas(comment)
    unaccented_comment = acentos_signos(lower_text)
    comment_tokens = tokenizar(unaccented_comment)
    filtered_sentence = eliminar_stop_words(comment_tokens)

    context = {'comment': comment,
               'lower_text': lower_text,
               'unaccented_comment': unaccented_comment,
               'comment_tokens': comment_tokens,
               'stopwords_remove': filtered_sentence}

    return context
