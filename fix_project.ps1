Write-Host "=== Исправление проекта AntiksHub ===" -ForegroundColor Cyan

# 1. Создаем недостающие файлы
Write-Host "`n1. Создаю недостающие файлы..." -ForegroundColor Yellow

# Создаем urls.py для каждого приложения
$apps = @("products", "users", "cart", "orders")
foreach ($app in $apps) {
    $urls_file = "$app\urls.py"
    if (!(Test-Path $urls_file)) {
        @"
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
"@ | Out-File -FilePath $urls_file -Encoding UTF8
        Write-Host "  Создан: $urls_file" -ForegroundColor Green
    }
}

# 2. Создаем простые views.py если их нет
foreach ($app in $apps) {
    $views_file = "$app\views.py"
    if (!(Test-Path $views_file) -or (Get-Item $views_file).Length -eq 0) {
        @"
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>$app - Страница в разработке</h1><p><a href="/">На главную</a></p>')
"@ | Out-File -FilePath $views_file -Encoding UTF8
        Write-Host "  Создан/обновлен: $views_file" -ForegroundColor Green
    }
}

# 3. Создаем упрощенный urls.py в главной папке
$main_urls = @"
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"@

Set-Content -Path "AntiksHub\urls.py" -Value $main_urls -Encoding UTF8
Write-Host "`n2. Упрощен главный urls.py" -ForegroundColor Green

# 4. Проверяем settings.py
$settings_path = "AntiksHub\settings.py"
$settings_content = Get-Content $settings_path -Raw

if ($settings_content -notmatch "'products'") {
    # Добавляем приложения в INSTALLED_APPS
    $new_settings = $settings_content -replace "('django.contrib.staticfiles',)", "`$1`n    'products',`n    'users',`n    'cart',`n    'orders',"
    Set-Content -Path $settings_path -Value $new_settings -Encoding UTF8
    Write-Host "3. Добавлены приложения в settings.py" -ForegroundColor Green
}

# 5. Создаем папки для медиа
$media_folders = @("media", "media\products", "media\avatars", "static")
foreach ($folder in $media_folders) {
    if (!(Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder -Force | Out-Null
        Write-Host "  Создана папка: $folder" -ForegroundColor Green
    }
}

# 6. Применяем миграции
Write-Host "`n4. Применяю миграции..." -ForegroundColor Yellow
python manage.py makemigrations
python manage.py migrate

Write-Host "`n=== Проект исправлен! ===" -ForegroundColor Cyan
Write-Host "`nЗапустите сервер:" -ForegroundColor White
Write-Host "python manage.py runserver" -ForegroundColor Yellow
Write-Host "`nОткройте в браузере:" -ForegroundColor White
Write-Host "http://127.0.0.1:8000/" -ForegroundColor Green
Write-Host "`nДля создания админа выполните:" -ForegroundColor White
Write-Host "python manage.py createsuperuser" -ForegroundColor Yellow