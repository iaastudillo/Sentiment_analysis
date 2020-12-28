from django.shortcuts import render
from sentimientos.models import *
from sentimientos.procesarDatos import *

# Create your views here.
def home(request):
    return render(request, 'sentimientos/home.html', {})


def probar_modelo(request):
    return render(request, 'sentimientos/probar_modelo.html', {})


def entrenar_modelo(request):
    if request.POST:

        comentario_post = request.POST['comentario_txt']

        if request.POST['flexRadio'] == 'positivo':
            clasificacion_post = 1
        if request.POST['flexRadio'] == 'neutro':
            clasificacion_post = 0
        if request.POST['flexRadio'] == 'negativo':
            clasificacion_post = -1

        context = procesar_comentario(comentario_post)

        comentario_final = ''
        for word in context['stopwords_remove']:
            comentario_final += word + " "

        c = Comentarios(comentario=comentario_post,
                        comentario_final=comentario_final,
                        clasificacion=clasificacion_post)
        c.save()

        print(comentario_post, comentario_final, clasificacion_post)

        return render(request, 'sentimientos/entrenar_modelo.html', context)
    else:
        return render(request, 'sentimientos/entrenar_modelo.html')


def alimentar_modelo(request):
    return render(request, 'sentimientos/alimentar_modelo.html', {})

