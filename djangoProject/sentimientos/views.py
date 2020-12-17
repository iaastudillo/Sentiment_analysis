from django.http import HttpResponseRedirect
from django.shortcuts import render
import nltk
from nltk.corpus import stopwords
import unidecode

# Create your views here.
def index(request):
    return render(request, 'sentimientos/index.html', {'saludo': 'hola mundo'})

def procearComentarios(request):
    comment = request.GET.get('text')
    #convierte a minúsculas
    lower_text = comment.lower()

    #quita los acentos
    unaccented_comment = unidecode.unidecode(lower_text)

    #toqueniza la frace
    tokenizer = nltk.RegexpTokenizer(r'\w+')
    comment_tokens = tokenizer.tokenize(unaccented_comment)

    #Elimina stop words
    stop_words = set(stopwords.words('spanish'))
    filtered_sentence = [w for w in comment_tokens if not w in stop_words]
    filtered_sentence = []
    for w in comment_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    print(comment_tokens)
    print(filtered_sentence)

    context = {'comment': comment,
               'lower_text': lower_text,
               'unaccented_comment': unaccented_comment,
               'comment_tokens': comment_tokens,
               'stopwords_remove': filtered_sentence}

    return render(request, 'sentimientos/procesar.html', context)
