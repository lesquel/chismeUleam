from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return redirect('register:login')
    if request.method == 'GET':
        return HttpResponse("Has enviado un formulario.")