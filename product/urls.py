# product/urls.py
from django.urls import path
from .views import ProductView, ProductTraceView

urlpatterns = [
    path('products/', ProductView.as_view(), name='list_create_products'),
    path('products/<int:pk>/', ProductView.as_view(), name='retrieve_update_delete_product'),
    path('products/top-products/<str:duration>/', ProductTraceView.as_view(),name='top-products'),
]
