"""Практическое занятие № 9, вариант 11: множества товаров."""

shops = {
    "Магнит": {"молоко", "соль", "сахар", "печенье", "сыр"},
    "Пятерочка": {"мясо", "молоко", "сыр"},
    "Перекресток": {"молоко", "творог", "сыр", "сахар", "печенье"},
    "Лента": {"печенье", "молоко", "сыр"},
}

print("Исходные данные:")
for shop, products in shops.items():
    print(f"{shop}: {', '.join(sorted(products))}")

print("\n1. Магазины, где нельзя купить соль:")
for shop, products in shops.items():
    if "соль" not in products:
        print(shop)

print("\n2. Магазины, где есть молоко, печенье и сыр:")
required = {"молоко", "печенье", "сыр"}
for shop, products in shops.items():
    if required.issubset(products):
        print(shop)

print("\n3. Магазины, где есть мясо и молоко:")
required = {"мясо", "молоко"}
for shop, products in shops.items():
    if required.issubset(products):
        print(shop)
