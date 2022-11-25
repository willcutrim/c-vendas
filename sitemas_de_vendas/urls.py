
from django.contrib import admin
from django.db import router
from django.urls import include, path

from rest_framework import routers

from vendas_app.viewset import CarrinhoViewSet

from rest_framework_simplejwt.views import (
  TokenObtainPairView,
  TokenRefreshView,
)

router = routers.DefaultRouter()
router.register('carrinho', CarrinhoViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vendas_app.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),


    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    
]
