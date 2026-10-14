"""Пример 1: пересечение и объединение множеств."""
magnit = {"хлеб", "молоко"}
troyka = {"хлеб", "сыр", "масло"}
karusel = {"хлеб", "сыр"}
print("Магнит:", sorted(magnit))
print("Тройка:", sorted(troyka))
print("Карусель:", sorted(karusel))
print("Продукты во всех магазинах:", sorted(magnit & troyka & karusel))
print("Все продукты в городе:", sorted(magnit | troyka | karusel))
