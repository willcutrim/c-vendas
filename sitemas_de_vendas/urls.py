
from django.contrib import admin
from django.db import router
from django.urls import include, path

from rest_framework import routers

from vendas_app.viewset import CarrinhoViewSet

router = routers.DefaultRouter()
router.register('carrinho', CarrinhoViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vendas_app.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
