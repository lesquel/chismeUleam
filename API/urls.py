from django.urls import path
from . import views

urlpatterns = [
    path('chismes', views.getAPIChismes, name='APIchismes'),
]