import os

# 1. Исправляем urls.py
urls_content = """from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""

with open("AntiksHub/urls.py", "w", encoding="utf-8") as f:
    f.write(urls_content)

# 2. Создаем views.py если нет
views_content = """from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
"""

with open("AntiksHub/views.py", "w", encoding="utf-8") as f:
    f.write(views_content)

# 3. Создаем папки шаблонов
os.makedirs("templates/products", exist_ok=True)

# 4. Создаем простые шаблоны
home_template = """<!DOCTYPE html>
<html>
<head>
    <title>AntiksHub - Маркетплейс 2026</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #FF6B35, #FF8E53);
            color: white;
            text-align: center;
            padding: 50px;
        }
        .container {
            background: rgba(255,255,255,0.1);
            padding: 40px;
            border-radius: 20px;
            backdrop-filter: blur(10px);
        }
        h1 { font-size: 48px; }
        a {
            color: white;
            text-decoration: none;
            background: rgba(255,255,255,0.2);
            padding: 10px 20px;
            border-radius: 25px;
            margin: 10px;
            display: inline-block;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🚀 AntiksHub работает!</h1>
        <p>Маркетплейс нового поколения 2026</p>
        <div>
            <a href="/admin/">⚙️ Админка</a>
            <a href="/products/">🛍️ Товары</a>
            <a href="/users/">👥 Пользователи</a>
        </div>
    </div>
</body>
</html>"""

with open("templates/home.html", "w", encoding="utf-8") as f:
    f.write(home_template)

products_template = """<!DOCTYPE html>
<html>
<head>
    <title>Товары - AntiksHub</title>
    <style>
        body { background: #f5f5f5; padding: 20px; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 30px; }
        h1 { color: #FF6B35; }
    </style>
</head>
<body>
    <div class="container">
        <h1>🛍️ Товары AntiksHub</h1>
        <p><a href="/">← На главную</a></p>
        <p>Страница товаров работает!</p>
        <p><a href="/admin/products/product/add/">Добавить товар через админку</a></p>
    </div>
</body>
</html>"""

with open("templates/products/list.html", "w", encoding="utf-8") as f:
    f.write(products_template)

print("✅ Все файлы исправлены!")
print("✅ Можно запускать сервер: python manage.py runserver")
