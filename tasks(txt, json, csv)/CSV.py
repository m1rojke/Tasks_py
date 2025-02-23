# Работа с CSV (таблицы)

# 🔹 Задание: Записать данные в CSV и считать их.

import csv

# Данные с пользователями
users = [
    ["Имя", "Возраст"],  # Заголовки
    ["Алекс", 25],
    ["Мария", 30],
    ["Иван", 22],
    ["Екатерина", 27],
    ["Дмитрий", 35]
]

# Запись в CSV-файл
with open("users.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(users)

# Чтение из CSV-файла и фильтрация
with open("users.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовок

    print("Пользователи старше 25 лет:")
    for row in reader:
        name, age = row[0], int(row[1])  # Преобразуем возраст в число
        if age > 25:
            print(f"{name}: {age} лет")