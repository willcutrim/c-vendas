from rest_framework import status
from django.shortcuts import redirect, render, HttpResponse
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Carrinho, Categoria, Produto
from .forms import FormProduto, FormCategoria
from .serializers import CarrinhoSerializer
from django.contrib import messages
import requests
from django.core.paginator import Paginator

class CarrinhoController(APIView):

    def get(self, request):
        produtos = Carrinho.objects.all()
        serializer = CarrinhoSerializer(produtos)
        return Response(serializer.data)


    def post(self, request):
        serializer = CarrinhoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)




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


def home(request):
    return render(request, 'html/home.html')

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


def vendas_detalhes(request, pk):
    venda = Carrinho.objects.get(pk=pk)
    produtos = ", ".join([str(p) for p in venda.produtos.all()])
    return render(request, 'html/venda-detalhe.html', {'venda':venda, 'produtos': produtos})

def caixa_vendas(request):
    produto = Produto.objects.all()
    
    total = float(0.0)
    qt = 0
    
    if request.method == 'POST':
        add = request.POST.getlist('produtos')
        
        url = 'https://w-vendas.herokuapp.com/api/carrinho/'
        q = calcular_venda(add)['quantidade']
        total = calcular_venda(add)['total']

        keyboard = {
            "valor_da_compra": total,
            "quantidade": q,
            "produtos": add,
        }
        response = requests.post(url, data=keyboard)

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



