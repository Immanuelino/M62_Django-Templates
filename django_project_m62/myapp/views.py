# myapp/views.py
from django.shortcuts import render
from datetime import datetime

def home_view(request):
    return render(request, 'home.html')

def filtered_view(request):
    texto = "¡Hola, Mundo!"
    fecha = datetime.now()
    return render(request, 'filtered_template.html', {'texto': texto, 'fecha': fecha})

def for_loop_view(request):
    numeros = list(range(1, 21))  # Lista de números del 1 al 20
    return render(request, 'for_loop_template.html', {'numeros': numeros})
