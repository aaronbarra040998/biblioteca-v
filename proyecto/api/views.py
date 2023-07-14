from rest_framework import generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from biblioteca.models import Autor, Categoria, Editorial, Libro
from .serializers import (
    AutorSerializer,
    CategoriaSerializer,
    EditorialSerializer,
    LibroSerializer,
)


class IndexView(APIView):
    def get(self, request):
        libros = Libro.objects.all()
        serializer_libro = LibroSerializer(libros, many=True)
        return Response(serializer_libro.data)


class AutorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Autor.objects.all()
    serializer_class = AutorSerializer


class AutorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Autor.objects.all()
    lookup_url_kwarg = "autor_id"
    serializer_class = AutorSerializer


class CategoriaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    lookup_url_kwarg = "categoria_id"
    serializer_class = CategoriaSerializer


class EditorialListCreateAPIView(generics.ListCreateAPIView):
    queryset = Editorial.objects.all()
    serializer_class = EditorialSerializer


class EditorialRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Editorial.objects.all()
    lookup_url_kwarg = "editorial_id"
    serializer_class = EditorialSerializer


class LibroViewSet(viewsets.ModelViewSet):
    queryset = Libro.objects.all()
    serializer_class = LibroSerializer
