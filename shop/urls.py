from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartViewSet, CartItemViewSet, OrderViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('products', ProductViewSet, basename='products')
router.register('carts', CartViewSet, basename='carts')
router.register('cart-items', CartItemViewSet, basename='cart-items')
router.register('orders', OrderViewSet, basename='orders')

urlpatterns = [
    path('', include(router.urls)),
    
]