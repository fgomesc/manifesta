from django.contrib.auth.decorators import login_required
from django.shortcuts import render




def home(request):
    return render(request, 'core/base.html')


@login_required
def index(request):
    return render(request, 'core/index.html')



