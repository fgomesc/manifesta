from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='core/logout.html'), name='logout'),
    path('', include('apps.core.urls')),
    path('usuario', include('apps.cadastro_usuario.urls')),
    path('pachamama/', include('apps.pachamama.urls')),
]
