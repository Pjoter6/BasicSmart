from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Light
from datetime import datetime


def strona_powitalna(request):
    return render(request, 'home_app/strona_powitalna.html')


def wybor_czujnika(request):
    return render(request, template_name='home_app/wybor_czujnika.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('wybor_czujnika')
        else:
            messages.error(request, 'Nieprawidłowa nazwa użytkownika lub hasło')
    return render(request, 'home_app/login.html')




def image_view(request):
    return render(request, 'home_app/image_view.html')

def light_view(request):
    light = Light.objects.first()
    if request.method == 'POST':
        action = request.POST.get('aktywacja')
        if action == '1':
            light.is_on = True
            light.last_activated = datetime.now()
        elif action =='0':
            light.is_on = False
        light.user = request.user
        light.save()






        return redirect('light_view')
    return render(request, 'home_app/light_view.html', {'light': light})


from django.shortcuts import render

def tabela_view(request):
    dane = [{"akcja": "Edytuj", "id": 1}, {"akcja": "Usuń", "id": 2}]
    return render(request, 'tabelaZarowka.html', {'dane': dane})
