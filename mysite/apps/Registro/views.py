from django.shortcuts import render, redirect
from .models import Libro, Profile
from .forms import LibroForm, CustomUserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

#rest_framework
from rest_framework import viewsets
from .serializers import LibroSerializer

# Create your views here.

def index(request):
    return render(request, 'App/index.html', {})


@login_required
def listado_libros(request):

    user = request.user
    libros = Libro.objects.filter(user=user)
    data={
        'libros': libros
    }
    return render(request, 'App/listado_libros.html', data)

@login_required
def agregar_libro(request):

    data={
        'form': LibroForm()
    }

    if request.method=='POST':
        formulario = LibroForm(request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario = formulario.save(commit=False)
            formulario.user = request.user
            formulario.save()
            data['mensaje']='Libro guardado correctamente'
        data['form']=formulario

    return render(request, 'App/agregar_libro.html', data)

@login_required
def modificar_libro(request, id):
    libro = Libro.objects.get(id=id)
    data ={
        'form': LibroForm(instance=libro)
    }

    if request.method=='POST':
        formulario = LibroForm(data=request.POST, instance=libro, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje']='Libro modificado correctamente'
        data['form']=LibroForm(instance=Libro.objects.get(id=id))

    return render(request,'App/modificar_libro.html', data)

@login_required
def eliminar_libro(request, id):

    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect(to='listado-libros')

@login_required
def eliminar_libro_busqueda(request, id):

    libro = Libro.objects.get(id=id)
    libro.delete()
    return redirect(to='busqueda')

@login_required
def visualizar_busqueda(request):

    titulo = request.GET.get('titulo')
    autor = request.GET.get('autor')
    libros= Libro.objects.all()

    if 'btn-titulo' in request.GET:
        if titulo:
            libros = Libro.objects.filter(titulo__icontains=titulo)
    elif 'btn-autor' in request.GET:
        if autor:
            libros = Libro.objects.filter(autor__icontains=autor)

    data={
        'libros': libros
    }

    return render(request, 'App/busqueda.html', data)

def registrar_usuario(request):

    data = {
        'form': CustomUserForm(),
        'profile': ProfileForm()
    }

    if request.method=='POST':

        formulario = CustomUserForm(request.POST)
        profile_form = ProfileForm(request.POST)

        if formulario.is_valid() and profile_form.is_valid():

            new_user = formulario.save()
            profile = profile_form.save(commit=False)
            profile.user = new_user
            profile.save()
            username=formulario.cleaned_data['username']
            password=formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect(to='index')
            
        data['form']=formulario
        data['profile']=profile_form

    return render(request, 'registration/registrar.html', data)

def perfil(request):

    user = request.user
    perfil = Profile.objects.get(user_id = user.id)
    data={      
        'perfil': perfil
    }
    return render(request, 'App/perfil.html', data)


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer