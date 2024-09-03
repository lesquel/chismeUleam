from django.shortcuts import render

# Create your views here.
def RegisterView(request):
    return render(request, 'register/pages/register.html')