from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import  login_required
from . import forms

# Create your views here.

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        checkbox = request.POST.get('checkbox')

        if password1 != password2:
            return JsonResponse({"error": "Las contraseñas no coinciden."})
        elif len(password1) < 8:
            return JsonResponse({"error": "La contraseña debe tener al menos 8 caracteres."})
        elif User.objects.filter(username=username).exists():
            return JsonResponse({"error": "El nombre de usuario ya está en uso."})
        elif checkbox != 'on':
            return JsonResponse({"error": "Debes aceptar los términos y condiciones."})

            return JsonResponse({"error": "El nombre de usuario ya está en uso."})
        elif checkbox != 'on':
            return JsonResponse({"error": "Debes aceptar los términos y condiciones."})

        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        
        return JsonResponse({"success": "Usuario creado exitosamente.", "redirect": reverse('main:home')})

    # Si el método es GET o cualquier otro, muestra la página de registro
    form = forms.SignUpForm()
    # Si el método es GET o cualquier otro, muestra la página de registro
    return render(request, 'register/pages/signup.html', {"form": form})


def login_view(request):
    
    #Si el usuario ya esta autenticado, lo redirige a la pagina principal
    if request.user.is_authenticated:
        return redirect('main:home')
    
    #Si el metodo es POST, valida los datos del formulario y loguea al usuario
    if request.method == 'POST':
        #Obtiene los datos del formulario
        username = request.POST['username']
        password = request.POST['password']
        
        #Obtiene datos del usuario y valida si existe 
        user = User.objects.filter(username=username).first()
        if user is None:
            return JsonResponse({"error": "El usuario no existe."})
        # Valida la contraseña del usuario
        user = authenticate(request, username=username, password=password)
        if user is None:
            return JsonResponse({"error": "La contraseña es incorrecta."})
        #Loguea al usuario y lo redirige a la pagina principal
        login(request, user)
        return JsonResponse({"success": "Sesión iniciada exitosamente.", "redirect": reverse('main:home')})
    
    form = forms.LoginForm()
    #Si el metodo es GET, muestra la pagina de login
    return render(request, 'register/pages/login.html', {"form": form})

@login_required
def logout_view(request):
    if request.method == 'GET': #hay que cambiar esto cuando este la opcion para logout
            messages.success(request, "Sesión cerrada exitosamente.")
            logout(request)
            return redirect('register:login')
