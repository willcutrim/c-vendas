from django import forms
from .models import Categoria, Produto

class FormCategoria(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = '__all__'

class FormProduto(forms.ModelForm):
    class Meta:
        model = Produto
        fields = '__all__'

