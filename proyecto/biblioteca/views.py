from django.shortcuts import render
from .models import Libro, Editorial, Autor, Categoria


def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'lista_libros.html', {'libros': libros})


def editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request, 'editoriales.html', {'editoriales': editoriales})

def autores(request):
    autores = Autor.objects.all()
    return render(request, 'autores.html', {'autores': autores})

def categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias.html', {'categorias': categorias})
