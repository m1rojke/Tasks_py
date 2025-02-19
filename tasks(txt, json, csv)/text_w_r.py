# 1. Работа с файлами

# Чтение и запись обычного текста (.txt)

# 🔹 Задание: Создать программу, которая записывает текст в файл и затем читает его.

# Запись в файл
with open("test.txt", "w", encoding="utf-8") as file:
    file.write("Hello my friend!")

# Чтение файла
with open("test.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print("Содержимое файла:", content)