import os
import sys

print("=== Исправление всех проблем AntiksHub ===")

# 1. Создаем правильный settings.py
settings_content = '''"""
Django settings for AntiksHub project.
"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-antikshub-2026-orange-marketplace'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
    'users',
    'cart',
    'orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AntiksHub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'AntiksHub.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
'''

with open("AntiksHub/settings.py", "w", encoding="utf-8") as f:
    f.write(settings_content)
print("✓ settings.py создан")

# 2. Создаем urls.py
urls_content = '''from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
'''

with open("AntiksHub/urls.py", "w", encoding="utf-8") as f:
    f.write(urls_content)
print("✓ urls.py создан")

# 3. Создаем views.py
views_content = '''from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
'''

with open("AntiksHub/views.py", "w", encoding="utf-8") as f:
    f.write(views_content)
print("✓ views.py создан")

# 4. Создаем папки и шаблоны
os.makedirs("templates/products", exist_ok=True)
os.makedirs("static/css", exist_ok=True)
os.makedirs("media/products", exist_ok=True)

# 5. Создаем домашнюю страницу
home_template = '''<!DOCTYPE html>
<html>
<head>
    <title>AntiksHub - Маркетплейс 2026</title>
    <style>
        :root {
            --orange-primary: #FF6B35;
            --orange-secondary: #FF8E53;
        }
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, var(--orange-primary), var(--orange-secondary));
            color: white;
            margin: 0;
            padding: 0;
        }
        .header {
            text-align: center;
            padding: 60px 20px;
        }
        h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }
        .nav {
            background: rgba(255,255,255,0.1);
            padding: 20px;
            margin: 20px auto;
            max-width: 800px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
        }
        .nav a {
            color: white;
            text-decoration: none;
            margin: 0 15px;
            padding: 10px 20px;
            background: rgba(255,255,255,0.2);
            border-radius: 25px;
            display: inline-block;
        }
        .nav a:hover {
            background: rgba(255,255,255,0.3);
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>🚀 AntiksHub</h1>
        <p>Маркетплейс нового поколения 2026</p>
        <p>Оранжевая тема • База продавцов и покупателей</p>
    </div>
    
    <div class="nav">
        <a href="/admin/">⚙️ Админка</a>
        <a href="/products/">🛍️ Товары</a>
        <a href="/users/">👥 Пользователи</a>
        <a href="/cart/">🛒 Корзина</a>
        <a href="/orders/">📦 Заказы</a>
    </div>
    
    <div class="container">
        <h2>Добро пожаловать в AntiksHub!</h2>
        <p>Ваш маркетплейс успешно запущен и готов к работе.</p>
        <p>Для начала работы перейдите в админ-панель и добавьте товары.</p>
    </div>
</body>
</html>'''

with open("templates/home.html", "w", encoding="utf-8") as f:
    f.write(home_template)
print("✓ home.html создан")

# 6. Создаем шаблон товаров
products_template = '''<!DOCTYPE html>
<html>
<head>
    <title>Товары - AntiksHub</title>
    <style>
        body {
            background: #f5f5f5;
            margin: 0;
            padding: 20px;
            font-family: Arial, sans-serif;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        h1 {
            color: #FF6B35;
            text-align: center;
        }
        .nav {
            text-align: center;
            margin: 20px 0;
        }
        .nav a {
            color: #FF6B35;
            text-decoration: none;
            margin: 0 10px;
            padding: 8px 16px;
            background: #fff3e0;
            border-radius: 20px;
        }
        .message {
            text-align: center;
            padding: 40px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🛍️ Каталог товаров</h1>
        <div class="nav">
            <a href="/">← На главную</a>
            <a href="/admin/products/product/add/">➕ Добавить товар</a>
        </div>
        <div class="message">
            <h3>Товары появятся здесь</h3>
            <p>Добавьте товары через админ-панель, и они появятся на этой странице.</p>
            <p><a href="/admin/" style="color: #FF6B35; font-weight: bold;">Перейти в админку</a></p>
        </div>
    </div>
</body>
</html>'''

with open("templates/products/list.html", "w", encoding="utf-8") as f:
    f.write(products_template)
print("✓ products/list.html создан")

# 7. Создаем простые views для всех приложений
apps = ["products", "users", "cart", "orders"]
for app in apps:
    # Создаем views.py
    app_views = f'''from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, '{app}/list.html')
'''
    with open(f"{app}/views.py", "w", encoding="utf-8") as f:
        f.write(app_views)
    
    # Создаем urls.py
    app_urls = '''from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
'''
    with open(f"{app}/urls.py", "w", encoding="utf-8") as f:
        f.write(app_urls)
    
    # Создаем шаблоны
    os.makedirs(f"templates/{app}", exist_ok=True)
    app_template = f'''<!DOCTYPE html>
<html>
<head>
    <title>{app.capitalize()} - AntiksHub</title>
    <style>
        body {{ background: #f5f5f5; padding: 20px; }}
        .container {{ max-width: 800px; margin: 0 auto; background: white; padding: 30px; }}
        h1 {{ color: #FF6B35; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{app.capitalize()}</h1>
        <p><a href="/">← На главную</a></p>
        <p>Страница {app} в разработке.</p>
    </div>
</body>
</html>'''
    
    with open(f"templates/{app}/list.html", "w", encoding="utf-8") as f:
        f.write(app_template)
    
    print(f"✓ Приложение {app} настроено")

print("\\n" + "="*50)
print("ВСЕ ПРОБЛЕМЫ ИСПРАВЛЕНЫ!")
print("="*50)
print("\\nДля запуска сервера выполните:")
print("python manage.py runserver")
print("\\nДля создания администратора:")
print("python manage.py createsuperuser")
