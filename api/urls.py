from django.contrib import admin
from django.urls import path
from catalog.views import CategoryListView, ProductListView  # Импорт из catalog
from api.views import CartView  # Импорт из api
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [

    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('cart/', CartView.as_view(), name='cart'),  # Добавление маршрута для корзины
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
