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
        form = forms.SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)
            return JsonResponse({
                "success": "Usuario creado exitosamente.",
                "redirect": reverse('main:home')
            })
        print(form.errors.as_json())
        return JsonResponse({"error": form.errors.as_json()}, status=400)

    # If the method is GET, show the signup form
    form = forms.SignUpForm()
    return render(request, 'register/pages/signup.html', {"form": form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('main:home')
    
    if request.method == 'POST':
        form = forms.LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return JsonResponse({
                "success": "Sesión iniciada exitosamente.",
                "redirect": reverse('main:home')
            })

        # Return form errors as JSON response
        return JsonResponse({"error": form.errors.as_json()}, status=400)
    
    form = forms.LoginForm()
    return render(request, 'register/pages/login.html', {"form": forms.LoginForm})



@login_required
def logout_view(request):
    if request.method == 'GET': #hay que cambiar esto cuando este la opcion para logout
            messages.success(request, "Sesión cerrada exitosamente.")
            logout(request)
            return redirect('register:login')
