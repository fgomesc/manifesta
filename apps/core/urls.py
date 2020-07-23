from django.urls import path
from .views import home, index

urlpatterns = [
    path('', home, name='home'),
    path('in/', index, name='index')

]
