from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import universidad,curso,programa_academicos, curso_programa
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
import datetime
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login

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
            return render(request, 'main.html',{ 'searchTerm':searchTerm, 'busqueda':universidades,'aux':1})
   
        elif(search=="programa"):
            programas=programa_academicos.objects.filter(nombre__icontains=searchTerm)
            universidades=[]
            for programa in programas:
                universidad1 = universidad.objects.filter(id_unico__icontains=programa.id_universidad.id_unico).first()
                universidades.append(universidad1)
            busqueda = zip(universidades, programas)
            return render(request, 'main.html',{ 'searchTerm':searchTerm, 'busqueda':busqueda ,'aux':2 })
    else:  
        universidades=universidad.objects.all()
        return render(request, 'main.html',{ 'searchTerm':searchTerm, 'busqueda':universidades,'aux':1})
   

def more_info(request,id_unico):
    universidad1 = universidad.objects.get(id_unico=id_unico)
    programas_academicos = programa_academicos.objects.filter(id_universidad=universidad1.id_unico)
    return render(request, 'more_info.html', {'universidad': universidad1, 'programas_academicos': programas_academicos})

def more_info_programa(request, id_unico):
    programa = programa_academicos.objects.get(id_unico=id_unico)
    curso_programas=curso_programa.objects.filter(id_programa_academico=id_unico)
    cursos=[]
    for curso1 in curso_programas:
        cursos+=curso.objects.filter(id_unico2=curso1.id_curso.id_unico2)
     
    return render(request, 'more_info_programa.html', {  'programa': programa , 'cursos' :cursos})

def register(request):  
    data = {'form':CustomUserCreationForm()}
    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            user= authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            return redirect('main')
        else:
            data["form"] = formulario
    return render(request, 'registration/register.html', data)

