from django.shortcuts import render
from .models import Task

def pagina_inicial(request):
    tasks = Task.objects.all()
    return render(request, "tasks/pagina_inicial.html", {"tasks": tasks})

def lista_tarefa(request):
    tasks = Task.objects.all()
    return render(request, "tasks/lista_tarefa.html")

def pagina_sobre(request):
    tasks = Task.objects.all()
    return render(request, "tasks/pagina_sobre.html", {'image_path': 'imagem\big_brain.jpg'})

def cadastros(request):
    tasks = Task.objects.all()
    return render(request, "tasks/cadastro.html")