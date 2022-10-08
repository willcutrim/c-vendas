
from django import forms
from .models import Categoria, Produto, Carrinho


class FormCategoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class FormProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

class FormCarrinho(forms.ModelForm):
    class Meta:
        model = Carrinho
        fields = ['produtos', 'quantidade', 'valor_da_compra']