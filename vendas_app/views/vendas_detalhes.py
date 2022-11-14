from django.shortcuts import render

from vendas_app.models import Carrinho


def vendas_detalhes(request, pk):
    venda = Carrinho.objects.get(pk=pk)
    produtos = ", ".join([str(p) for p in venda.produtos.all()])
    return render(request, 'html/venda-detalhe.html', {'venda':venda, 'produtos': produtos})