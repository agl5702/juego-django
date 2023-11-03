from django.shortcuts import render
from .models import Pregunta, Respuesta

# Create your views here.



def Juego(request):

        pregunta= Pregunta.objects.all()
        respuesta = Respuesta.objects.all()

        context = {'preguntas': pregunta,
        'respuestas': respuesta,
        }
        return render(request,'preguntas/index.html', context)