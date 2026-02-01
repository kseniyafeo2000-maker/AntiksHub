import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AntiksHub.settings')
django.setup()

from django.contrib.auth.models import User
from products.models import Product

# Создаем тестового продавца
seller, created = User.objects.get_or_create(
    username='seller1',
    defaults={'email': 'seller1@antikshub.ru'}
)
if created:
    seller.set_password('seller123')
    seller.save()

# Создаем тестовые товары
products_data = [
    {
        'name': 'Смартфон Orange X2026',
        'description': 'Современный смартфон с оранжевым корпусом, 2026 года выпуска',
        'price': 45999.00,
        'seller': seller
    },
    {
        'name': 'Ноутбук Django Pro',
        'description': 'Мощный ноутбук для разработки на Django',
        'price': 89999.00,
        'seller': seller
    },
    {
        'name': 'Книга "Python для начинающих"',
        'description': 'Лучшая книга для изучения Python',
        'price': 2499.00,
        'seller': seller
    },
    {
        'name': 'Оранжевая футболка AntiksHub',
        'description': 'Фирменная футболка маркетплейса',
        'price': 1899.00,
        'seller': seller
    },
]

for data in products_data:
    Product.objects.get_or_create(**data)

print("✅ Тестовые данные созданы!")
print("Продавец: seller1 / seller123")
print("Админ: admin / ваш_пароль")