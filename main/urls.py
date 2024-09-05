from django.urls import path
from . import views

# Define the app name para poder acceder a las urls de este archivo desde cualquier template con
# la sintaxis 'app_name:url_name'
app_name = 'main'

urlpatterns = [
    path('', views.home_view, name='home'),
]
