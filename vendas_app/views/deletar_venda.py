from django.shortcuts import redirect
from vendas_app.models import Carrinho


def deletar_venda(request, pk):
    if request.method == 'POST':
        id_venda = Carrinho.objects.get(pk=pk)
        id_venda.delete()
        return redirect('/historico-vendas')