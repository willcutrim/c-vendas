from django.contrib import messages
from django.shortcuts import redirect, render


from vendas_app.forms import FormProduto
from vendas_app.models import Produto


def cadastro_produtos(request):
    produtos = Produto.objects.all()
    if request.method == 'POST':
        form = FormProduto(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto adcionado com sucesso')
            return redirect('/cadastrar_produtos')
    else:
        form = FormProduto()
    return render(request, 'html/produtos.html', {'form': form, 'produtos': produtos})