from django.shortcuts import render,redirect
from pyexpat.errors import messages
from django.contrib.auth import authenticate, login



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
            # Przekieruj do strony głównej po pomyślnym logowaniu
            return redirect('home')
        else:
            messages.error(request, 'Nieprawidłowa nazwa użytkownika lub hasło')
    return render(request, 'login.html')