from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    return render(request, 'students/index.html')

def dashboard(request):
    return render(request, 'students/dashboard.html')

def mentor(request):
    return render(request, 'students/mentor.html')

def cursos(request):
    return render(request, 'students/cursos.html')

def perfil(request):
    return render(request, 'students/perfil.html')

def cursos_andamento(request):
    return render(request, 'students/cursos_andamento.html')

def planos_estudo(request):
    return render(request, 'students/planos_estudo.html')

def projetos(request):
    return render(request, 'students/projetos.html')

def entrevistas(request):
    return render(request, 'students/entrevistas.html')

def matricula(request):
    return render(request, 'students/matricula.html')

def login(request):
    return render(request, 'students/login.html')

def sobre(request):
    return render(request, 'cv/index.html')
