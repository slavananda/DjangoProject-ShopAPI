from django.contrib import admin
from django.urls import path, include  # Обязательно импортируем include
from catalog.views import CategoryListView, ProductListView  # Импорты для каталога
from django.http import HttpResponse

# Это просто временный ответ для корневого пути
def home(request):
    return HttpResponse("<h1>Welcome to the API Home</h1>")


urlpatterns = [
    path('', home, name='home'),  # Добавляем маршрут для пустого пути
    path('admin/', admin.site.urls),
    path('categories/', CategoryListView.as_view(), name='category-list'),  # Из catalog/views.py
    path('products/', ProductListView.as_view(), name='product-list'),      # Из catalog/views.py
    path('', include('api.urls')),  # Подключаем маршруты из api/urls.py
]
