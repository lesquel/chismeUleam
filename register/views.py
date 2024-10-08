from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import  login_required
from . import forms

# Create your views here.

def signup_view(request):
    # Si el usuario ya esta autenticado, redirigir a la pagina principal
    if request.user.is_authenticated:
        return redirect('main:home')

    # Si el metodo es POST, procesar el formulario de registro
    if request.method == 'POST':
        form = forms.SignUpForm(data=request.POST)
        # Si el formulario es valido, crear el usuario y redirigir a la pagina principal
        if form.is_valid():
            user = form.save()  
            login(request, user)
            return JsonResponse({
                "success": "Usuario creado exitosamente.",
                "redirect": reverse('main:home')
            })
        # Si el formulario no es valido, retornar los errores en formato JSON
        return JsonResponse({"error": form.errors.as_json()})

    # Si el metodo es GET, retornar el formulario de registro
    form = forms.SignUpForm()
    return render(request, 'register/pages/signup.html', {"form": form})


def login_view(request):
    # Si el usuario ya esta autenticado, redirigir a la pagina principal
    if request.user.is_authenticated:
        return redirect('main:home')
    # Si el metodo es POST, procesar el formulario de inicio de sesion
    if request.method == 'POST':
        form = forms.LoginForm(data=request.POST)
        # Si el formulario es valido, iniciar sesion y redirigir a la pagina principal
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Si el checkbox de recordar sesion no esta marcado, la sesion expira al cerrar el navegador
            if not request.POST.get('checkbox'):
                request.session.set_expiry(0)
                
            return JsonResponse({
                "success": "Sesión iniciada exitosamente.",
                "redirect": reverse('main:home')
            })

        print(form.errors.as_json())
        # Si el formulario no es valido, retornar los errores en formato JSON
        return JsonResponse({"error": form.errors.as_json()})
    
    form = forms.LoginForm()
    return render(request, 'register/pages/login.html', {"form": forms.LoginForm})



@login_required
def logout_view(request):
    if request.method == 'GET': #hay que cambiar esto cuando este la opcion para logout
            messages.success(request, "Sesión cerrada exitosamente.")
            logout(request)
            return redirect('register:login')
