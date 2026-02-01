import os

# Создаем папки
os.makedirs("templates/products", exist_ok=True)

# Создаем главный шаблон
home_template = '''<!DOCTYPE html>
<html>
<head>
    <title>AntiksHub - Маркетплейс 2026</title>
    <style>
        body { background: #FF6B35; color: white; padding: 50px; text-align: center; }
        h1 { font-size: 48px; }
        a { color: white; margin: 0 15px; }
    </style>
</head>
<body>
    <h1>🚀 AntiksHub</h1>
    <p>Маркетплейс нового поколения 2026</p>
    <div style="margin: 30px;">
        <a href="/admin/">⚙️ Админка</a>
        <a href="/products/">🛍️ Товары</a>
    </div>
    <p>Проект успешно работает!</p>
</body>
</html>'''

with open("templates/home.html", "w", encoding="utf-8") as f:
    f.write(home_template)

# Создаем шаблон товаров
products_template = '''<!DOCTYPE html>
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
        <h1>Товары</h1>
        <p><a href="/">← На главную</a></p>
        <p>Здесь будут товары...</p>
    </div>
</body>
</html>'''

with open("templates/products/list.html", "w", encoding="utf-8") as f:
    f.write(products_template)

print("Шаблоны созданы!")
