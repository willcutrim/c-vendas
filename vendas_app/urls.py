from django.urls import path
from . import views
urlpatterns = [
    path('', views.vendas),


    path('cadastrar_categoria', views.cadastrar_categoria, name='cadastrar_categoria'),
    path('cadastrar_produtos', views.cadastro_produtos, name='cadastrar_produtos'),

    path('historico-vendas', views.historico_de_vendas, name='historico-vendas'),


    path('venda-detalhe/<int:pk>', views.vendas_detalhes, name='venda-detalhe')
]