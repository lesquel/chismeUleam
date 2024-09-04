from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import  login_required


# Create your views here.
def signup_view(request):
    #Si el usuario ya esta autenticado, lo redirige a la pagina principal
    if request.user.is_authenticated:
        return redirect('main:home')
    #Si el metodo es POST, valida los datos del formulario y crea el usuario
    if request.method == 'POST':
        #Obtiene los datos del formulario
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        terminos = request.POST.get('terminos')
        
        #Valida los datos del formulario y muestra mensajes de error si es necesario
        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'register/pages/signup.html')
        elif len(password1) < 8:
            messages.error(request, "La contraseña debe tener al menos 8 caracteres.")
            return render(request, 'register/pages/signup.html')
        elif User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return render(request, 'register/pages/signup.html')
        elif terminos != 'on':
            messages.error(request, "Debes aceptar los términos y condiciones.")
            return render(request, 'register/pages/signup.html')
        
        #Crea el usuario usando el modelo User de Django y automaticamente lo loguea, 
        # para despues redirigirlo a la pagina principal
        user = User.objects.create_user(username=username, password=password1)
        login(request, user)
        messages.success(request, "Usuario creado exitosamente.")
        return redirect('main:home')
    #Si el metodo es GET, muestra la pagina de registro
    return render(request, 'register/pages/signup.html')

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
            messages.error(request, "El usuario no existe.")
            return render(request, 'register/pages/login.html')
        # Valida la contraseña del usuario
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "La contraseña es incorrecta.")
            return render(request, 'register/pages/login.html')
        #Loguea al usuario y lo redirige a la pagina principal
        login(request, user)
        messages.success(request, "Sesión iniciada exitosamente.")
        return redirect('main:home')
    
    #Si el metodo es GET, muestra la pagina de login
    return render(request, 'register/pages/login.html')

@login_required
def logout_view(request):
    if request.method == 'GET': #hay que cambiar esto cuando este la opcion para logout
            messages.success(request, "Sesión cerrada exitosamente.")
            logout(request)
            return redirect('register:login')
