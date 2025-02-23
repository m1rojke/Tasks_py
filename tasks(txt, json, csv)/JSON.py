# Работа с JSON

# 🔹 Задание: Записать и считать данные в JSON-формате.

import json

# Данные с пользователями
users = [
    {"name": "Алекс", "age": 25},
    {"name": "Мария", "age": 30},
    {"name": "Иван", "age": 22}
]

# Запись в JSON-файл
with open("users.json", "w", encoding="utf-8") as file:
    json.dump(users, file, indent=4, ensure_ascii=False)

# Чтение из JSON-файла
with open("users.json", "r", encoding="utf-8") as file:
    loaded_users = json.load(file)

# Вывод возраста каждого пользователя
print("Возраст пользователей:")
for user in loaded_users:
    print(f"{user['name']}: {user['age']} лет")