from django.contrib import admin
from .models import Categoria, Produto, Carrinho
admin.site.register(Categoria)
admin.site.register(Produto)
admin.site.register(Carrinho)

# @admin.register(Carrinho)
# class CarrinhoAdmin(admin.ModelAdmin):
#     lista=['data_compra','written_by']