from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Carrinho

from .serializers import CarrinhoSerializer


class CarrinhoController(APIView):

    def get(self, request):
        produtos = Carrinho.objects.all()
        serializer = CarrinhoSerializer(produtos)
        return Response(serializer.data)


    def post(self, request):
        serializer = CarrinhoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)