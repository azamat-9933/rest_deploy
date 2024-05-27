from django.urls import path

from products.views import *


urlpatterns = [
    path('home/', ProductListAPIView.as_view(), name="product-list"),
    path('<int:pk>/', ProductDetailAPIView.as_view(), name="product-detail"),
    path('orders/', CreateOrderAPIView.as_view(), name='create-order'),
    path('manufactures/', ManufacturerListAPIView.as_view(), name='manufactures'),
    path('categories/', CategoryListAPIView.as_view(), name='categories'),
    path('', ProductFilterListAPIView.as_view(), name='product-filter')
]