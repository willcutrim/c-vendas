from tabnanny import verbose
from django.db import models


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=150, verbose_name='Nome da categoria')

    def __str__(self):
        return self.nome_categoria

class Produto(models.Model):
    nome = models.CharField(max_length=150, blank=False, null=False)
    preco_do_produto = models.DecimalField(decimal_places=2, blank=False, null=False, max_digits=6)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    desc = models.TextField(max_length=250, blank=True, null=True)


    def __str__(self):
        return self.nome



class Carrinho(models.Model):
    produtos = models.ManyToManyField(Produto, blank=True, related_name='vendas')
    data_compra = models.DateTimeField(auto_now_add=True)
    valor_da_compra = models.DecimalField(decimal_places=2, max_digits=10, default=0, blank=True)
    quantidade = models.IntegerField()

    
    def __str__(self):
        
        return str(self.data_compra)
