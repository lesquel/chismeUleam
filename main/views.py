from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    if not request.user.is_authenticated:
        return HttpResponse("No tienes permiso para ver esta página.")
    if request.method == 'GET':
        return HttpResponse("Has enviado un formulario.")