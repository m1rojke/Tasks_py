# 3. Работа с requests (запросы в интернет)

# 🔹 Задание: Запросить курсы валют с сайта https://api.exchangerate-api.com.

import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"

try:
    response = requests.get(url)
    response.raise_for_status()  # Проверяем, нет ли ошибки HTTP
    data = response.json()
    print("Курс доллара к евро:", data["rates"]["EUR"])
except requests.exceptions.RequestException as e:
    print("Ошибка при запросе:", e)


# ✅ Практика:

    # Найди API, который дает прогноз погоды.
    # Запроси и выведи прогноз.
