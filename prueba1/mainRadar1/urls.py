
from django.urls import path
from .views import home,main,exit,more_info, register, more_info_programa

urlpatterns = [
    path('', home, name='home'),
    path('main/', main, name='main'),
    path('logout/',exit, name='exit'),
    path('main/more_info/<int:id_unico>/',more_info, name='more_info'),
    path('main/more_info/more_info_programa/<int:id_unico>/',more_info_programa, name='more_info_programa'),
    path('register/', register, name='register'),

    
]