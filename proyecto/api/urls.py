from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    IndexView,
    AutorListCreateAPIView,
    AutorRetrieveUpdateDestroyAPIView,
    CategoriaListCreateAPIView,
    CategoriaRetrieveUpdateDestroyAPIView,
    EditorialListCreateAPIView,
    EditorialRetrieveUpdateDestroyAPIView,
    LibroViewSet,
)

# Configurar el enrutador
router = DefaultRouter()
router.register(r'libros', LibroViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='api-index'),
    path('autores/', AutorListCreateAPIView.as_view(), name='api-autor-list'),
    path('autores/<int:autor_id>/', AutorRetrieveUpdateDestroyAPIView.as_view(), name='api-autor-detail'),
    path('categorias/', CategoriaListCreateAPIView.as_view(), name='api-categoria-list'),
    path('categorias/<int:categoria_id>/', CategoriaRetrieveUpdateDestroyAPIView.as_view(), name='api-categoria-detail'),
    path('editoriales/', EditorialListCreateAPIView.as_view(), name='api-editorial-list'),
    path('editoriales/<int:editorial_id>/', EditorialRetrieveUpdateDestroyAPIView.as_view(), name='api-editorial-detail'),
    path('libros/', LibroViewSet.as_view({'post': 'create'}), name='api-libro-create'),  # Agregar esta línea
    path('admin/', include(router.urls)),
]
