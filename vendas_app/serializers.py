
from rest_framework import serializers
from .models import Carrinho

class CarrinhoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrinho
        fields = '__all__'