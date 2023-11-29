from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,"layout.html")

def cursos(request):
    cursos = ['Lenguaje de Programación 3', 'Legislación Informática', 
                'Ingeniería de Requerimientos', 'Algoritmos de Computación Gráfica',
                'Microprocesadores', 'Gestión de Procesos de Negocios', 'Dinámica de Sistemas']
    return render(request, 'cursos.html', {'cursos': cursos})