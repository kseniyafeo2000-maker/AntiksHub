# add_products_simple.py
import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AntiksHub.settings')
django.setup()

from django.contrib.auth.models import User
from products.models import Category, Product

print("=== Добавление товаров в AntiksHub ===")

# Определяем товары для добавления
products_to_add = [
    {
        'name': 'Смартфон iPhone 16 Pro Orange 512GB',
        'description': 'Флагманский смартфон Apple- это лучшее решение для повседневной жизни и занятий фотографией. Мощный процессор так же может справляться с разными задачами.',
        'price': 156990.00,
        'category_name': 'Электроника',
        'seller_username': 'prodam_vse',
        'stock': 10    },
    {
        'name': ' ASUS ROG Zephyrus GU605MV, 16"',
        'description': 'Игровой ноутбук ASUS ROG Zephyrus G16 GU605MV-QR259 - идеальный выбор для геймеров, ценящих высокую производительность и потрясающую графику.',
        'price': 660138.00,
        'category_name': 'Электроника',
        'seller_username': 'prodam_vse',
        'stock': 3
    },
    {
        'name': 'Футболка Burberry',
        'description': 'Футболка хлопковая с принтом',
        'price': 58 794.00,
        'category_name': 'Одежда',
        'seller_username': 'brend_odezhda',
        'stock': 8
    },
    {
        'name': 'Игровая консоль PlayStation 5',
        'description': 'Новейшая игровая консоль Sony с 4K графикой',
        'price': 79999.99,
        'category_name': 'Игры',
        'seller_username': 'prodam_vse',
        'stock': 7
    },
    {
        'name': 'Кофемашина DeLonghi Magnifica',
        'description': 'Автоматическая кофемашина для дома',
        'price': 44999.99,
        'category_name': 'Дом и сад',
        'seller_username': 'prodam_vse',
        'stock': 4
    },
]

print(f"Будет добавлено {len(products_to_add)} товаров...")

for i, product_data in enumerate(products_to_add, 1):
    try:
        # Получаем или создаем категорию
        category, created = Category.objects.get_or_create(
            name=product_data['category_name'],
            defaults={'slug': product_data['category_name'].lower()
                     .replace('📱', '').replace('👕', '').replace('📚', '')
                     .replace('🎮', '').replace('🏠', '').strip()
                     .replace(' ', '-').replace('"', '')}
        )
        
        # Получаем продавца
        seller = User.objects.get(username=product_data['seller_username'])
        
        # Создаем товар
        product, created = Product.objects.get_or_create(
            name=product_data['name'],
            defaults={
                'description': product_data['description'],
                'price': product_data['price'],
                'category': category,
                'seller': seller,
                'stock': product_data['stock'],
                'is_active': True
            }
        )
        
        if created:
            print(f"{i}. ✅ Добавлен: {product.name} - {product.price} ₽ (Остаток: {product.stock} шт.)")
        else:
            print(f"{i}. ℹ️ Уже существует: {product.name}")
            
    except User.DoesNotExist:
        print(f"{i}. ❌ Ошибка: Пользователь {product_data['seller_username']} не найден")
    except Exception as e:
        print(f"{i}. ❌ Ошибка: {str(e)}")

print(f"\n=== ИТОГО ===")
print(f"Всего товаров в базе: {Product.objects.count()}")
print(f"Активных товаров: {Product.objects.filter(is_active=True).count()}")
print(f"Средняя цена: {Product.objects.all().aggregate(models.Avg('price'))['price__avg']:.2f} ₽")
