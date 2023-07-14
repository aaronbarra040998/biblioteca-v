from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('categorias/', views.categorias, name='categorias'),
    path('editoriales/', views.editoriales, name='editoriales'),
    path('autores/', views.autores, name='autores'),
]