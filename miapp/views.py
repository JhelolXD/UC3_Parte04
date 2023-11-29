from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request,"layout.html")

def cursos(request):
    cursos = ['Lenguaje de Programación 3', 'Legislación Informática', 
                'Ingeniería de Requerimientos', 'Algoritmos de Computación Gráfica',
                'Microprocesadores', 'Gestión de Procesos de Negocios', 'Dinámica de Sistemas']
    return render(request, 'cursos.html', {'cursos': cursos})

def es_primo(request,a=0,b=100):
    primos = []
    if a > b:
        return redirect('primos', a=b, b=a)
    
    for i in range(a,b+1):
        contador = 0
        for j in range(1,i+1):
            if i % j == 0:
                contador += 1
        if contador == 2:
            primos.append(i)

    return render(request,'primos.html',{'primos':primos,'a':a,'b':b})

def examen(request):
    examen = [
        {'name': 'Ayquipa Estrada Jheremy William', 'github' : 'https://github.com/JhelolXD/UC3_Parte01.git'},
        {'name': 'Urbisagastegui Huamani Jhon Antony', 'github' : 'https://github.com/UnUrbiSalvaje/UC3_Parte02'},
        {'name': 'Talledo Vega Samuel Elias', 'github' : 'https://github.com/Santrax211/UC3-Parte03.git'},
        {'name': 'Ayquipa Estrada Jheremy William', 'github' : 'https://github.com/JhelolXD/UC3_Parte04.git'},
        
    ]
    return render(request, 'examen.html', {'examen': examen})