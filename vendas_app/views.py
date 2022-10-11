from math import prod
from django.shortcuts import redirect, render
from django.contrib import messages


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
    total = 0
    for i in produto:
        
        total = i.preco_do_produto + i.preco_do_produto

    print(total, i.nome)
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
    
    return render(request, 'html/vendas.html', {'vendas': vendas})


def vendas_detalhes(request, pk):
    venda = Carrinho.objects.get(pk=pk)
    produtos = ", ".join([str(p) for p in venda.produtos.all()])
    return render(request, 'html/venda-detalhe.html', {'venda':venda, 'produtos': produtos})
