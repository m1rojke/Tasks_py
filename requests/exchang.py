# 3. Работа с requests (запросы в интернет)

# 🔹 Задание: Запросить курсы валют с сайта https://api.exchangerate-api.com.

import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
data = response.json()

print("Курс доллара к евро:", data["rates"]["EUR"])

# ✅ Практика:

    # Найди API, который дает прогноз погоды.
    # Запроси и выведи прогноз.
    
