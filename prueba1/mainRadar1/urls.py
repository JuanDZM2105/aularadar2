
from django.urls import path
from .views import home,main,exit,more_info, register

urlpatterns = [
    path('', home, name='home'),
    path('main/', main, name='main'),
    path('logout/',exit, name='exit'),
    path('mainscreen/more_info/<int:id_unico>/',more_info, name='more_info'),
    path('register/', register, name='register'),

    
]