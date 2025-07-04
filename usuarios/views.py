from django.shortcuts import render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django

def login(request):
    if request.method=="GET":
        return render(request, 'usuarios/login.html')
    else:
        username=request.POST.get('email')
        senha=request.POST.get('senha')

        user=authenticate(username=username, password=senha)

        if user:
            login_django(request,user)
            return HttpResponse('Autenticado!')
        
        else:
            return HttpResponse('E-mail ou senha inválidos!')
        
def cadastro(request):
    if request.method=="GET":
        return render(request, 'usuarios/cadastro.html')
    else:
        username=request.POST.get('email')
        email=request.POST.get('email')
        password=request.POST.get('senha')
        first_name=request.POST.get('nome')

        user=User.objects.filter(username=username).first()

        if user:
            return HttpResponse('usuário já existente!')
        else:
            user=User.objects.create_user(username=username, email=email, password=password, first_name=first_name)
            user.save()

            return HttpResponse('Usuário cadastrado com sucesso!')

def home(request):
    return render(request, 'usuarios/home.html')

def lancar(request):
    return render(request, 'usuarios/lancar.html')

def alterar(request):
    return render(request, 'usuarios/alterar.html')

def visualizar(request):
    return render(request, 'usuarios/visualizar.html')    