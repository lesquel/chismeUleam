from django.shortcuts import render
from django.http import JsonResponse    
# Create your views here.
def getAPIChismes(request):
    
    return JsonResponse({"chismes": "hola"})