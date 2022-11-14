from django.shortcuts import render, redirect
from django.contrib import messages

from vendas_app.forms import FormCategoria
from vendas_app.models import Categoria


def cadastrar_categoria(request):
    categorias = Categoria.objects.all()
    if request.method == 'POST':
        form  = FormCategoria(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria adicionada com sucesso')
            return redirect('/')
    else:
        form = FormCategoria()
    return render(request, 'html/categorias.html', {'form': form, 'categorias': categorias})