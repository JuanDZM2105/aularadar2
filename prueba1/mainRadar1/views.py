from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import universidad,curso,programa_academicos
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime
from .forms import CustomUserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def exit(request):
    logout(request)
    return redirect('home')

@login_required
def main(request):
    searchTerm=request.GET.get('searchUniversity')
    search=request.GET.get('busqueda')
    if searchTerm:
        if(search=="universidad"):
            universidades=universidad.objects.filter(nombre__icontains=searchTerm)
            
        elif(search=="curso"):
            universidades=curso.objects.filter(nombre__icontains=searchTerm)
             
        elif(search=="programa"):
            universidades=programa_academicos.objects.filter(nombre__icontains=searchTerm)
        return render(request, 'main.html',{ 'searchTerm':searchTerm, 'universidades':universidades})
    else:  
        return render(request, 'main.html')
    

def more_info(request,id_unico):
    universidad1 = get_object_or_404(universidad, id_unico=id_unico)
    return render(request, 'more_info.html', {'universidad': universidad1})

def register(request):
    data = {'form':CustomUserCreationForm()}
    return render(request, 'registration/register.html', data)

