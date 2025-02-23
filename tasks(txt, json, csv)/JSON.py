# Работа с JSON

# 🔹 Задание: Записать и считать данные в JSON-формате.

import json

# Данные с пользователями
users = [
    {"name": "Алекс", "age": 25},
    {"name": "Мария", "age": 30},
    {"name": "Иван", "age": 22}
]

# Пытаемся считать файл, если он есть
try:
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)  # Загружаем JSON
    print("Данные из файла:", data)
except FileNotFoundError:
    print("Файл не найден! Создаю новый...")
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4, ensure_ascii=False)  # Записываем `users`
    data = users  # Используем записанные данные

# Вывод возраста каждого пользователя
print("Возраст пользователей:")
for user in data:
    print(f"{user['name']}: {user['age']} лет")