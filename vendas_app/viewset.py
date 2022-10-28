from rest_framework import viewsets

from .serializers import CarrinhoSerializer
from .models import Carrinho

class CarrinhoViewSet(viewsets.ModelViewSet):
    queryset = Carrinho.objects.all()
    serializer_class = CarrinhoSerializer