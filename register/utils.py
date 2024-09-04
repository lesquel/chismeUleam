from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Validaciones simples
        if password1 != password2:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya está en uso.")
            return render(request, 'register.html')

        if User.objects.filter(email=email).exists():
            messages.error(request, "El correo electrónico ya está en uso.")
            return render(request, 'register.html')

        # Crear el usuario
        user = User.objects.create_user(username=username, email=email, password=password1)
        login(request, user)
        messages.success(request, "Usuario creado exitosamente.")
        return redirect('home')

    return render(request, 'register.html')
