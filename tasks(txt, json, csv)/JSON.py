# Работа с JSON

# 🔹 Задание: Записать и считать данные в JSON-формате.

import json

data = {"name": "Алекс",
        "age": 25,
        "city": "Moscow",
        }

# Запись в JSON
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

# Чтение JSON
with open("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print("Прочитанные данные:", loaded_data)