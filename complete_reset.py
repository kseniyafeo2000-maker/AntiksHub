# complete_reset.py
import os
import shutil

print("=== ПОЛНЫЙ СБРОС AntiksHub ===")

# 1. Удаляем базу данных
if os.path.exists('db.sqlite3'):
    os.remove('db.sqlite3')
    print("🗑️ База данных удалена")

# 2. Удаляем все миграции
apps = ['products', 'users', 'cart', 'orders']
for app in apps:
    migrations_dir = os.path.join(app, 'migrations')
    if os.path.exists(migrations_dir):
        for file in os.listdir(migrations_dir):
            if file != '__init__.py' and file.endswith('.py'):
                os.remove(os.path.join(migrations_dir, file))
        print(f"🗑️ Миграции {app} удалены")

# 3. Создаем простые модели
print("📝 Создаю простые модели...")

# products/models.py
with open('products/models.py', 'w', encoding='utf-8') as f:
    f.write('''from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self): return self.name

class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    stock = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    def __str__(self): return self.name
''')

# users/models.py
with open('users/models.py', 'w', encoding='utf-8') as f:
    f.write('''from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True)
    def __str__(self): return self.user.username
''')

# cart/models.py  
with open('cart/models.py', 'w', encoding='utf-8') as f:
    f.write('''from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Корзина {self.user.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    def __str__(self): return f"{self.product.name} x{self.quantity}"
''')

# orders/models.py
with open('orders/models.py', 'w', encoding='utf-8') as f:
    f.write('''from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f"Заказ #{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self): return f"{self.product.name} x{self.quantity}"
''')

# 4. Создаем простые admin.py файлы
with open('products/admin.py', 'w', encoding='utf-8') as f:
    f.write('''from django.contrib import admin
from .models import Category, Product
admin.site.register(Category)
admin.site.register(Product)
''')

with open('users/admin.py', 'w', encoding='utf-8') as f:
    f.write('''# Пустой файл - User уже зарегистрирован в auth
from django.contrib import admin
''')

with open('cart/admin.py', 'w', encoding='utf-8') as f:
    f.write('''from django.contrib import admin
from .models import Cart, CartItem
admin.site.register(Cart)
admin.site.register(CartItem)
''')

with open('orders/admin.py', 'w', encoding='utf-8') as f:
    f.write('''from django.contrib import admin
from .models import Order, OrderItem
admin.site.register(Order)
admin.site.register(OrderItem)
''')

print("✅ Все файлы созданы!")
print("\nТеперь выполните следующие команды:")
print("1. python manage.py makemigrations")
print("2. python manage.py migrate")
print("3. python manage.py createsuperuser")
print("4. python manage.py runserver")
