from django.core.paginator import Paginator
from django.shortcuts import render


from vendas_app.models import Carrinho


def historico_de_vendas(request):
    vendas_q = Carrinho.objects.filter().order_by('-data_compra')
    p = Paginator(vendas_q, 10)
    page = request.GET.get('page')
    vendas = p.get_page(page)

    
    start_date = request.GET.get('data_inicial')
    end_date = request.GET.get('data_final')
    if start_date and end_date:
        vendas = Carrinho.objects.filter(data_compra__range=[start_date, end_date])
    
    return render(request, 'html/vendas.html', {'vendas_q': vendas_q, 'vendas': vendas, 'p': p})