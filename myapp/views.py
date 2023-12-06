# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Producto

@login_required
def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'myapp/catalogo.html', {'productos': productos})
