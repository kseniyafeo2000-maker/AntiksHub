import os

print("Настройка AntiksHub...")

# Создаем папки
for folder in ["media", "static"]:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"Создана папка: {folder}")

# Создаем простой views.py для products
products_views = '''from django.http import HttpResponse

def index(request):
    return HttpResponse("Products page")
'''
with open('products/views.py', 'w') as f:
    f.write(products_views)

# Создаем простой urls.py для products
products_urls = '''from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
]
'''
with open('products/urls.py', 'w') as f:
    f.write(products_urls)

# Создаем главный urls.py
main_urls = '''from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>AntiksHub</h1><p>Welcome!</p>")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('products/', include('products.urls')),
]
'''
with open('AntiksHub/urls.py', 'w') as f:
    f.write(main_urls)

print("Готово!")
