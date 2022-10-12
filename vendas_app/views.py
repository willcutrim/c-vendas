from django.shortcuts import redirect, render
from django.contrib import messages
from pyparsing import empty


from .models import Carrinho, Categoria, Produto
from .forms import FormCarrinho, FormProduto, FormCategoria



def cadastrar_categoria(request):
    if request.method == 'POST':
        form  = FormCategoria(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Produto adcionado com sucesso')
            return redirect('/')
    else:
        form = FormCategoria()
    return render(request, 'html/categorias.html', {'form': form})


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


def vendas(request):
    produto = Produto.objects.all()
    if request.method == 'POST':
        form = FormCarrinho(request.POST)
        if form.is_valid():
            # form.save()
            return redirect('/')
    else:
        form = FormCarrinho()
    return render(request, 'html/home.html', {'form': form, 'produtos': produto})

def historico_de_vendas(request):
    vendas = Carrinho.objects.all()
    vendas_q = Carrinho.objects.filter()
    
    start_date = request.GET.get('data_inicial')
    end_date = request.GET.get('data_final')
    if start_date and end_date:
        vendas_q = Carrinho.objects.filter(data_compra__range=[start_date, end_date])
    
    return render(request, 'html/vendas.html', {'vendas': vendas, 'vendas_q': vendas_q})


def vendas_detalhes(request, pk):
    venda = Carrinho.objects.get(pk=pk)
    produtos = ", ".join([str(p) for p in venda.produtos.all()])
    return render(request, 'html/venda-detalhe.html', {'venda':venda, 'produtos': produtos})

def caixa_vendas(request):
    produto = Produto.objects.all()
    if request.method == 'POST':
        form = FormCarrinho(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/caixa-vendas')
    else:
        form = FormCarrinho()
    return render(request, 'html/caixa-vendas.html', {'form': form, 'produtos': produto})
