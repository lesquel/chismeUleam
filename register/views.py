from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.models import User


# Create your views here.
def signup_view(request):
    # Si el usuario esta autenticado, redirige a la pagina principal
    if request.user.is_authenticated:
        return redirect('main:home')
    # Si el usuario no esta autenticado, muestra el formulario de registro
    if request.method == 'POST':
        # Obtenemos los datos del formulario
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        terminos = request.POST.get('terminos')

        # Comprobamos que las contraseñas sean iguales
        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'register/pages/signup.html')
        # Comprobamos que la contraseña tenga al menos 8 caracteres
        if len(password1) < 8:
            messages.error(request, "La contraseña debe tener al menos 8 caracteres.")
            return render(request, 'register/pages/signup.html')
        # Comprobamos que el nombre de usuario no este en uso
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return render(request, 'register/pages/signup.html')
        # Comprobamos que el usuario acepte los términos y condiciones
        if terminos != 'on':
            messages.error(request, "Debes aceptar los términos y condiciones.")
            return render(request, 'register/pages/signup.html')
        # Creamos el usuario
        user = User.objects.create_user(username=username, password=password1)
        # Iniciamos sesión
        login(request, user)
        # Mostramos un mensaje de exito
        messages.success(request, "Usuario creado exitosamente.")
        return redirect('main:home')
        
    return render(request, 'register/pages/signup.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = User.objects.filter(username=username).first()
        if user is None:
            messages.error(request, "El usuario no existe.")
            return render(request, 'register/pages/login.html')
        
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "La contraseña es incorrecta.")
            return render(request, 'register/pages/login.html')
        
        login(request, user)
        messages.success(request, "Sesión iniciada exitosamente.")
        return redirect('main:home')
    
    return render(request, 'register/pages/login.html')

def logout_view(request):
    if request.method == 'GET': #hay que cambiar esto cuando este la opcion para logout
        if request.user.is_authenticated:
            messages.success(request, "Sesión cerrada exitosamente.")
            logout(request)
            redirect('register:login')
        else:
            messages.error(request, "No hay ninguna sesión activa.")
            return redirect('register:login')
    return redirect('register:login')
