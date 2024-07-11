from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomRegistroForm

# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def registro(request):
    if request.method == 'POST':
        form = CustomRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            auth_login(request, user)
            return redirect('inicio')  # Redirigir a la página principal después del registro
    else:
        form = CustomRegistroForm()
    return render(request, 'registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('inicio')  # Redirigir a la página principal después del inicio de sesión
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    auth_logout(request)
    return redirect('inicio')  # Redirigir a la página principal después del cierre de sesión


def libretas(request):
    return render(request,'libretas.html')

def marca_paginas(request):
    return render(request,'marca_paginas.html')

def tacos_notas(request):
    return render(request,'tacos_notas.html')