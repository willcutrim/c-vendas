from django.urls import path


from vendas_app.views.cadastrar_categoria import cadastrar_categoria
from vendas_app.views.cadastrar_produtos import cadastro_produtos
from vendas_app.views.historico_de_vendas import historico_de_vendas
from vendas_app.views.vendas_detalhes import vendas_detalhes
from vendas_app.views.caixa_vendas import caixa_vendas
from vendas_app.views.home import home
from vendas_app.views.deletar_venda import deletar_venda
from vendas_app.views.login import login
from vendas_app.views.registrar import registrar

from .viewset import CarrinhoViewSet

urlpatterns = [
    path('', home, name='home'),


    path('cadastrar_categoria', cadastrar_categoria, name='cadastrar_categoria'),
    path('cadastrar_produtos', cadastro_produtos, name='cadastrar_produtos'),
    path('historico-vendas', historico_de_vendas, name='historico-vendas'),
    path('venda-detalhe/<int:pk>', vendas_detalhes, name='venda-detalhe'),

    path('caixa-vendas', caixa_vendas, name='caixa-vendas'),

    path('vender/', CarrinhoViewSet.as_view),


    path('deletar-venda/<int:pk>', deletar_venda, name='deletar-venda'),

    path('login', login, name='login'),
    path('registrar', registrar, name='registrar'),

]