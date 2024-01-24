# views.py
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ParseError
from .models import Product
from .serializer import ProductSerializer
from django.utils import timezone
class ProductView(APIView):
    def post(self, request):
        return self.create_product(request)

    def put(self, request, pk):
        return self.update_product(request, pk)

    def get(self, request):
        return self.list_all_products(request)

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return Response("Product Deleted Successfully")

    def create_product(self, request):
        serializer = ProductSerializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ParseError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        response_data = serializer.data
        return Response(response_data, status=status.HTTP_201_CREATED)

    def update_product(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        serializer = ProductSerializer(product, data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except ParseError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        response_data = serializer.data
        return Response(response_data, status=status.HTTP_200_OK)

    def list_all_products(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ProductTraceView(APIView):

    def get(self, request, duration):
        present = timezone.now()

        if duration == 'all':
            products = Product.objects.order_by('-trace_count')[:5]
        elif duration == 'lastDay':
            yesterday = present - timezone.timedelta(days=1)
            products = Product.objects.filter(trace_date__gte=yesterday).order_by('-trace_count')[:5]

        elif duration == 'lastWeek':
            last_week = present - timezone.timedelta(days=7)
            products = Product.objects.filter(
                trace_date__gte=last_week
            ).order_by('-trace_count')[:5]
        else:
            return Response({'error': 'Invalid parameter', 'Options' : 'all, lastDay, lastWeek'}, status=400)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

