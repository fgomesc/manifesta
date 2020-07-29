from django.urls import path
from .views import UsuarioCreate


urlpatterns = [
    path('', UsuarioCreate.as_view(), name='create_usuario'),
]