from django.shortcuts import render

# Create your views here.
def RegiterView(request):
    return render(request, 'register/register.html')