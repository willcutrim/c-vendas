from django.shortcuts import redirect, render
import requests
from django.contrib import messages

from vendas_app.models import Produto


def caixa_vendas(request):
    produto = Produto.objects.all()
    
    total = float(0.0)
    qt = 0
    
    if request.method == 'POST':
        add = request.POST.getlist('produtos')
        # url_base = 'http://127.0.0.1:8000/'
        url_base = 'https://w-vendas.herokuapp.com/api/carrinho/'
        q = calcular_venda(add)['quantidade']
        total = calcular_venda(add)['total']

        keyboard = {
            "valor_da_compra": total,
            "quantidade": q,
            "produtos": add,
        }

        response = requests.post(url_base, data=keyboard)
        
        if response.status_code == 201:
            messages.info(request, 'Valor da compra R$ {}'.format(total))
            return redirect('/caixa-vendas')
        
    return render(request, 'html/caixa-vendas.html', {'produtos': produto, 'total': total, 'quantidade': qt})



def calcular_venda(add):
    total = float(0)
    
    for i in add: 
        q = Produto.objects.get(pk=i)
        total += float(q.preco_do_produto)
    
    q = len(add)
    
    return {'quantidade': q, 'total': total}