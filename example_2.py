"""Пример 2: добавление элемента во множество."""
colors = {"red", "green", "blue"}
print("Исходное множество:", sorted(colors))
if "yellow" not in colors:
    colors.add("yellow")
print("Изменённое множество:", sorted(colors))
