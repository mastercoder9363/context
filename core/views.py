from django.shortcuts import render
from .models import Gul, Barg

def index(request):
    gullar = Gul.objects.all()
    barglar = Barg.objects.all()
    context = {
        'gullar': gullar,
        'barglar': barglar
    }
    return render(request, 'index.html', context)